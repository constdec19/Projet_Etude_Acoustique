import pandas as pd
import matplotlib.pyplot as plt
import math
from matplotlib.pyplot import *
import os
from statistics import mean
from scipy import signal

dossier = 'Test/R1/R-1/'
#Fichier à étudier
nom_fichier = 'R1-R-1_TS-02134_2021-05-07-18-28-16_aligned'

### Création des dossiers
if not os.path.exists(dossier+nom_fichier+'/Spectrogramm/ax'):
 os.makedirs(dossier+nom_fichier+'/Spectrogramm/ax')
if not os.path.exists(dossier+nom_fichier+'/Spectrogramm/ay'):
 os.makedirs(dossier+nom_fichier+'/Spectrogramm/ay')
if not os.path.exists(dossier+nom_fichier+'/Spectrogramm/az'):
 os.makedirs(dossier+nom_fichier+'/Spectrogramm/az')

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/CSV/ax')
list2 = os.listdir(dossier+nom_fichier+'/CSV/ay')
list3 = os.listdir(dossier+nom_fichier+'/CSV/az')


### Spectrogrammes pour les ax
j = 0
liste_nom = []
liste_intensitemax = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/CSV/ax/'+i)
    # Normalisation
    y_ax = data_x['ax'] - mean(data_x['ax'])
    y_ax_normalisé = y_ax / max([max(y_ax), abs(min(y_ax))])
    Te = data_x['t'][1] - data_x['t'][0]  # Période d'échantillonage
    Fe = 1 / Te  # Fréquence d'échantillonage
    fig, ax = plt.subplots()
    powerSpectrum, freqenciesFound, time, imageAxis = ax.specgram(y_ax_normalisé, Fs=Fe)
    N = len(powerSpectrum)
    plt.xlabel('Temps en s')
    plt.title(nom_fichier)
    plt.ylabel('Fréquence en Hz')
    fig.colorbar(imageAxis).set_label('Intensité')
    plt.savefig(dossier+nom_fichier+'/Spectrogramm/ax'+ '/spectrogramm_ax_'+str(j) + '.png')
    plt.close()

    #Intensité maximale
    db = 10 * np.log10(powerSpectrum)
    intmax = np.max(db[8:])
    liste_intensitemax.append(intmax)
    liste_nom.append('coupe_' + str(j))
    j = j + 1

#Enregistrement des intensités maximales
df_ax = pd.DataFrame({'numero': liste_nom, 'intensitemax': liste_intensitemax}, columns=['numero', 'intensitemax'])
df_ax.to_csv(dossier + nom_fichier + '/Spectrogramm/ax/' + 'intensitemax_ax_.csv', index=False)


liste_intensitemax = []
### Spectrogrammes pour les ay
j = 0
for i in list2:
    data_y = pd.read_csv(dossier+nom_fichier+'/CSV/ay/'+i)
    # Normalisation
    y_ay = data_y['ay'] - mean(data_y['ay'])
    y_ay_normalisé = y_ay / max([max(y_ay), abs(min(y_ay))])
    Te = data_y['t'][1] - data_y['t'][0]  # Période d'échantillonage
    Fe = 1 / Te  # Fréquence d'échantillonage
    fig, ax = plt.subplots()
    powerSpectrum, freqenciesFound, time, imageAxis = ax.specgram(y_ay_normalisé, Fs=Fe)
    plt.xlabel('Temps en s')
    plt.title(nom_fichier)
    plt.ylabel('Fréquence en Hz')
    fig.colorbar(imageAxis).set_label('Intensité')
    plt.savefig(dossier+nom_fichier+'/Spectrogramm/ay'+ '/spectrogramm_ay_'+str(j) + '.png')

    #Intensité maximale
    db = 10 * np.log10(powerSpectrum)
    intmax = np.max(db[8:])
    liste_intensitemax.append(intmax)
    j = j + 1

#Enregistrement des intensités maximales
df_ax = pd.DataFrame({'numero': liste_nom, 'intensitemax': liste_intensitemax}, columns=['numero', 'intensitemax'])
df_ax.to_csv(dossier + nom_fichier + '/Spectrogramm/ay/' + 'intensitemax_ay_.csv', index=False)


### Spectrogrammes pour les az
j = 0
liste_intensitemax = []
for i in list3:
    data_z = pd.read_csv(dossier+nom_fichier+'/CSV/az/'+i)
    # Normalisation
    y_az = data_z['az'] - mean(data_z['az'])
    y_az_normalisé = y_az / max([max(y_az), abs(min(y_az))])
    Te = data_z['t'][1] - data_z['t'][0]  # Période d'échantillonage
    Fe = 1 / Te  # Fréquence d'échantillonage
    fig, ax = plt.subplots()
    powerSpectrum, freqenciesFound, time, imageAxis = ax.specgram(y_az_normalisé, Fs=Fe)
    plt.xlabel('Temps en s')
    plt.title(nom_fichier)
    plt.ylabel('Fréquence en Hz')
    fig.colorbar(imageAxis).set_label('Intensité')
    plt.savefig(dossier+nom_fichier+'/Spectrogramm/az'+ '/spectrogramm_az_'+str(j) + '.png')
    plt.close()

    #Intensité maximale
    db = 10 * np.log10(powerSpectrum)
    intmax = np.max(db[8:])
    liste_intensitemax.append(intmax)
    j = j + 1

#Enregistrement des intensités maximales
df_ax = pd.DataFrame({'numero': liste_nom, 'intensitemax': liste_intensitemax}, columns=['numero', 'intensitemax'])
df_ax.to_csv(dossier + nom_fichier + '/Spectrogramm/az/' + 'intensitemax_az_.csv', index=False)







