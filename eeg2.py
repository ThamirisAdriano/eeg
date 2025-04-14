import os
import mne
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. Carregar o EEG com MNE
sample_file = '/Users/thamirisadriano/Downloads/Neuro - Base de dados/chb-mit/chb-mit-scalp-eeg-database-1.0.0/chb01/chb01_03.edf'
raw = mne.io.read_raw_edf(sample_file, preload=True)

# 2. Anotar uma crise epiléptica (simulando labels)
seizure_start = 2996
seizure_end = 3036
duration = seizure_end - seizure_start
annotations = mne.Annotations(onset=[seizure_start], duration=[duration], description=['seizure'])
raw.set_annotations(annotations)

# 3. Criar janelas de 5s e rotular com base na anotação
def extrair_janelas_e_rotulos(raw, janela=5, sfreq=256):
    X, y = [], []
    total_tempo = int(raw.times[-1])
    for start in range(0, total_tempo - janela, janela):
        segment = raw.copy().crop(start, start + janela)
        data, _ = segment.get_data(return_times=True)
        features = np.mean(data, axis=1)  # Feature simples: média de cada canal
        X.append(features)
        # Verifica se esse trecho tem crise
        tem_crise = any([(start >= onset) and (start <= onset + dur)
                         for onset, dur in zip(raw.annotations.onset, raw.annotations.duration)])
        y.append(1 if tem_crise else 0)
    return np.array(X), np.array(y)

# 4. Extrair features e rótulos
X, y = extrair_janelas_e_rotulos(raw)

# 5. Treinar e avaliar modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Relatório de classificação:")
print(classification_report(y_test, y_pred))
