import os
import pandas as pd
import numpy as np

nom_fichier = 'R3-R-1_TS-02123_2021-05-07-18-28-12_aligned'
dossier = 'Test/R3/R-1/'

### Création des dossiers
if not os.path.exists(dossier+nom_fichier+'/Centroid/ax'):
 os.makedirs(dossier+nom_fichier+'/Centroid/ax')
if not os.path.exists(dossier+nom_fichier+'/Centroid/ay'):
 os.makedirs(dossier+nom_fichier+'/Centroid/ay')
if not os.path.exists(dossier+nom_fichier+'/Centroid/az'):
 os.makedirs(dossier+nom_fichier+'/Centroid/az')

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/CSV/ax')
list2 = os.listdir(dossier+nom_fichier+'/CSV/ay')
list3 = os.listdir(dossier+nom_fichier+'/CSV/az')



### Centroid pour les ax
j = 0
liste_nom = []
liste_centroid = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/CSV/ax/'+i)
    # Affichage du Spectre
    N = data_x['ax'].shape[-1]  # Nombre d'échantillons
    window = np.hamming(N)  # Fenêtre de Hamming
    Te = data_x['t'][1] - data_x['t'][0]  # Période d'échantillonage
    Fe = 1 / Te  # Fréquence d'échantillonage
    sp = np.fft.fft(data_x['ax'] * window)  # Spectre
    sp = np.fft.fftshift(sp)  # replacer le spectre dans le bon ordre avant(0->pos,neg->0) après (neg->0,0->pos)
    f = np.linspace(-Fe / 2, Fe / 2, N)  # table des fréquences
    n = len(f)
    f = f[n // 2:]  # que les valeurs positives

    spectrum = np.abs(sp[n // 2:])
    spectral_centroid = np.sum(f * spectrum) / np.sum(spectrum)
    liste_centroid.append(spectral_centroid)
    liste_nom.append('coupe_'+str(j))
    j = j + 1

# Enregistrement au format CSV
df_ax = pd.DataFrame({'numero': liste_nom, 'centroid': liste_centroid}, columns=['numero', 'centroid'])
df_ax.to_csv(dossier + nom_fichier + '/Centroid/ax/' + 'centroides_ax_.csv')

### Centroid pour les ay
j = 0
liste_nom = []
liste_centroid = []
for i in list2:
    data_y = pd.read_csv(dossier+nom_fichier+'/CSV/ay/'+i)
    # Affichage du Spectre
    N = data_y['ay'].shape[-1]  # Nombre d'échantillons
    window = np.hamming(N)  # Fenêtre de Hamming
    Te = data_y['t'][1] - data_y['t'][0]  # Période d'échantillonage
    Fe = 1 / Te  # Fréquence d'échantillonage
    sp = np.fft.fft(data_y['ay'] * window)  # Spectre
    sp = np.fft.fftshift(sp)  # replacer le spectre dans le bon ordre avant(0->pos,neg->0) après (neg->0,0->pos)
    f = np.linspace(-Fe / 2, Fe / 2, N)  # table des fréquences
    n = len(f)
    f = f[n // 2:]  # que les valeurs positives
    spectrum = np.abs(sp[n // 2:])
    spectral_centroid = np.sum(f * spectrum) / np.sum(spectrum)
    liste_centroid.append(spectral_centroid)
    liste_nom.append('coupe_'+str(j))
    j = j + 1

# Enregistrement au format CSV
df_ay = pd.DataFrame({'numero': liste_nom, 'centroid': liste_centroid}, columns=['numero', 'centroid'])
df_ay.to_csv(dossier + nom_fichier + '/Centroid/ay/' + 'centroides_ay_.csv')

### Centroid pour les az
j = 0
liste_nom = []
liste_centroid = []
for i in list3:
    data_z = pd.read_csv(dossier+nom_fichier+'/CSV/az/'+i)
    # Affichage du Spectre
    N = data_z['az'].shape[-1]  # Nombre d'échantillons
    window = np.hamming(N)  # Fenêtre de Hamming
    Te = data_z['t'][1] - data_z['t'][0]  # Période d'échantillonage
    Fe = 1 / Te  # Fréquence d'échantillonage
    sp = np.fft.fft(data_z['az'] * window)  # Spectre
    sp = np.fft.fftshift(sp)  # replacer le spectre dans le bon ordre avant(0->pos,neg->0) après (neg->0,0->pos)
    f = np.linspace(-Fe / 2, Fe / 2, N)  # table des fréquences
    n = len(f)
    f = f[n // 2:]  # que les valeurs positives

    spectrum = np.abs(sp[n // 2:])
    spectral_centroid = np.sum(f * spectrum) / np.sum(spectrum)
    liste_centroid.append(spectral_centroid)
    liste_nom.append('coupe_'+str(j))
    j = j + 1

# Enregistrement au format CSV
df_az = pd.DataFrame({'numero': liste_nom, 'centroid': liste_centroid}, columns=['numero', 'centroid'])
df_az.to_csv(dossier + nom_fichier + '/Centroid/az/' + 'centroides_az_.csv')


