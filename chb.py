import os
import mne
import matplotlib.pyplot as plt

sample_file = '/Users/thamirisadriano/Downloads/Neuro - Base de dados/chb-mit/chb-mit-scalp-eeg-database-1.0.0/chb01/chb01_03.edf'

seizure_start = 2996
seizure_end = 3036

raw = mne.io.read_raw_edf(sample_file, preload=True)
print("Arquivo carregado.")

# Adicionar anotação da crise
duration = seizure_end - seizure_start
onset = seizure_start
description = 'Seizure'
annotations = mne.Annotations(onset=onset, duration=duration, description=description)
raw.set_annotations(annotations)

# Cortar apenas o trecho com a crise + alguns segundos antes e depois
raw_crop = raw.copy().crop(seizure_start - 5, seizure_end + 5)

fig = raw_crop.plot(n_channels=10, title='EEG com crise epiléptica (CHB01_03)', show=False)
fig.savefig("eeg_chbmit_seizure.png", dpi=300)
print("Imagem salva como eeg_chbmit_seizure.png")
