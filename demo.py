import mne

# Caminho para o novo arquivo com crise
sample_file = '/Users/thamirisadriano/Downloads/Neuro - Base de dados/chb-mit/chb-mit-scalp-eeg-database-1.0.0/chb05/chb05_06.edf'

# Marcação da crise epiléptica
seizure_start = 1732
seizure_end = 1772
duration = seizure_end - seizure_start

# Carregar EEG
raw = mne.io.read_raw_edf(sample_file, preload=True)
print("Arquivo carregado.")

# Adicionar anotação da crise
annotations = mne.Annotations(onset=[seizure_start], duration=[duration], description=['seizure'])
raw.set_annotations(annotations)

# Cortar o trecho com a crise e alguns segundos extras
raw_crop = raw.copy().crop(seizure_start - 5, seizure_end + 5)

# Plotar o gráfico
raw_crop.plot(n_channels=10, title="EEG com crise epiléptica (chb05_06)", show=True)
