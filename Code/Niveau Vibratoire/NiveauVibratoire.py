import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


## Fichier à étudier
nom_fichier = 'R3-CD-1_TS-02134_2021-05-07-18-28-13_aligned'
dossier = 'Test/R3/CD-1/'

### Création des dossiers
if not os.path.exists(dossier+nom_fichier+'/NVibratoire/ax'):
 os.makedirs(dossier+nom_fichier+'/NVibratoire/ax')
if not os.path.exists(dossier+nom_fichier+'/NVibratoire/ay'):
 os.makedirs(dossier+nom_fichier+'/NVibratoire/ay')
if not os.path.exists(dossier+nom_fichier+'/NVibratoire/az'):
 os.makedirs(dossier+nom_fichier+'/NVibratoire/az')

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/CSV/ax')
list2 = os.listdir(dossier+nom_fichier+'/CSV/ay')
list3 = os.listdir(dossier+nom_fichier+'/CSV/az')


### Niveau vibratoire pour les ax
j = 0  #Pour le nom du fichier sauvegarder
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/CSV/ax/'+i)
    Vdbx = 20 * np.log10(np.abs(data_x['ax'])/10**(-6))

    # Pour enregistrer la figure

    # plt.xlabel('Temps en s')
    # plt.ylabel('Vdb (Vref=0.000001s² m/s²)')
    # plt.plot(data_x['t'], Vdbx)
    # plt.savefig(dossier+nom_fichier+'/NVibratoire/ax'+ '/vibratoire_ax_'+str(j) + '.png')
    #plt.close()

    # Enregistrer les valeurs
    df_ax = pd.DataFrame({'t': data_x['t'], 'Vdbx': Vdbx}, columns=['t', 'Vdbx'])
    df_ax.to_csv(dossier + nom_fichier + '/NVibratoire/ax/' + 'nvibratoire_ax_'+str(j)+'.csv')
    j = j + 1

### Niveau Vibratoire pour les ay
j = 0
for i in list2:
    data_y = pd.read_csv(dossier+nom_fichier+'/CSV/ay/'+i)
    Vdby = 20 * np.log10(np.abs(data_y['ay']/10**(-6)))

    # Pour enregistrer la figure

    # plt.xlabel('Temps en s')
    # plt.ylabel('Vdb (Vref=0.000001s² m/s²)')
    # plt.plot(data_y['t'], Vdby)
    # plt.savefig(dossier+nom_fichier+'/NVibratoire/ay'+ '/vibratoire_ay_'+str(j) + '.png')
    # plt.close()

    # Enregistrer les valeurs
    df_ay = pd.DataFrame({'t': data_y['t'], 'Vdby': Vdby}, columns=['t', 'Vdby'])
    df_ay.to_csv(dossier + nom_fichier + '/NVibratoire/ay/' + 'nvibratoire_ay_'+str(j)+'.csv')
    j = j + 1


### Niveau Vibratoire pour les az
j = 0
for i in list3:
    data_z = pd.read_csv(dossier+nom_fichier+'/CSV/az/'+i)
    Vdbz = 20 * np.log10(data_z['az'] / 10 ** (-6))

    # Pour enregistrer la figure

    # plt.xlabel('Temps en s')
    # plt.ylabel('Vdb (Vref=0.000001s² m/s²)')
    # plt.plot(data_z['t'], Vdbz)
    # plt.savefig(dossier+nom_fichier+'/NVibratoire/az'+ '/vibratoire_az_'+str(j) + '.png')
    # plt.close()

    # Enregistrer les valeurs
    df_az = pd.DataFrame({'t': data_z['t'], 'Vdbz': Vdbz}, columns=['t', 'Vdbz'])
    df_az.to_csv(dossier + nom_fichier + '/NVibratoire/az/' + 'nvibratoire_az_'+str(j)+'.csv')
    j = j + 1
