import mne
import neurokit2 as nk
import matplotlib.pyplot as plt

sample_file = '/Users/thamirisadriano/Downloads/Neuro - Base de dados/chb-mit/chb-mit-scalp-eeg-database-1.0.0/chb01/chb01_03.edf'
raw = mne.io.read_raw_edf(sample_file, preload=True)

canal = 0
nome_canal = raw.ch_names[canal]
data, times = raw[canal]  #

eeg_signal = data[0]
sfreq = int(raw.info['sfreq'])

cleaned = nk.signal_filter(eeg_signal, sampling_rate=sfreq, lowcut=0.5, highcut=40, method='butterworth', order=5)

nk.signal_plot([eeg_signal, cleaned], labels=["Original", "Filtrado (0.5–40Hz)"])
plt.suptitle(f"Canal {nome_canal} – Filtro NeuroKit2")
plt.savefig("eeg_canal_filtrado.png", dpi=300)


print("Imagem salva como eeg_canal_limpo.png")
