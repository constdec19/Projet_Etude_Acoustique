from scipy.io.wavfile import read
import statistics
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dossier = 'Plat/plat3'
nom_fichier = 'plat3'
data = pd.read_csv(nom_fichier+'.csv')

if not os.path.exists(dossier +'/spectrogramme'):
 os.makedirs(dossier +'/spectrogramme')
if not os.path.exists(dossier +'/centroid'):
 os.makedirs(dossier +'/centroid')
if not os.path.exists(dossier +'/Nsonore'):
 os.makedirs(dossier +'/Nsonore')


####Spectrogramme
Te = data['t'][1] - data['t'][0]  # Période d'échantillonage
Fe = 1 / Te  # Fréquence d'échantillonage

fig, ax = plt.subplots()
powerSpectrum, freqenciesFound, time, imageAxis = ax.specgram(data['x'], Fs=Fe)
plt.xlabel('Temps en s')
plt.title(nom_fichier)
plt.ylabel('Fréquence en Hz')
fig.colorbar(imageAxis).set_label('Intensité')
#plt.savefig(dossier+'/spectrogramme/'+nom_fichier+'.png')
plt.show()
db = 10 * np.log10(powerSpectrum)
intmax = np.max(db[8:])
df_ax = pd.DataFrame({'nom': [nom_fichier], 'intensitemax': [intmax]}, columns=['nom', 'intensitemax'])
df_ax.to_csv(dossier + '/spectrogramme/'+nom_fichier+'_intensitemax.csv')

###Centroid
N = data['x'].shape[-1]  # Nombre d'échantillons
window = np.hamming(N)  # Fenêtre de Hamming
sp = np.fft.fft(data['x'] * window)  # Spectre
sp = np.fft.fftshift(sp)  # replacer le spectre dans le bon ordre avant(0->pos,neg->0) après (neg->0,0->pos)
f = np.linspace(-Fe / 2, Fe / 2, N)  # table des fréquences

n = len(f)
plt.plot(f[n // 2-1:],np.abs(sp)[n // 2-1:])
plt.show()
f = f[n // 2:]  # que les valeurs positives

spectrum = np.abs(sp[n // 2:])
spectral_centroid = np.sum(f * spectrum) / np.sum(spectrum)
df_ax = pd.DataFrame({'nom': [nom_fichier], 'centroid': [spectral_centroid]}, columns=['nom', 'centroid'])
df_ax.to_csv(dossier + '/centroid/'+nom_fichier+'_centroid.csv')


###Niveau sonore

Vdb = 20 * np.log10(np.abs(data['x'])/(2*10**(-5)))  #Pa
df_ax = pd.DataFrame({'t': data['t'], 'db': Vdb}, columns=['t', 'db'])
df_ax.to_csv(dossier +'Nsonore'+ nom_fichier +'_nsonore.csv')
