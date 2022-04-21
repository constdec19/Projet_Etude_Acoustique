import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Fichier à découper
nom_fichier = 'R2-CD-1_TS-02105_2021-05-07-18-28-39_aligned'
data = pd.read_csv('Fichiers/'+nom_fichier+'.csv')
# Dossier où l'on veut placer le résultat
dossier = 'Test/R2/CD-1/'


####### Listes des temps auquel il y a eu une frappe par nom de fichier ######
#R1 CD-1
#x = [2.071,6.033,10.060,14.069, 18.088, 22.071, 26.097,31.020,35.036, 39.003, 45.008, 49.098, 53.104,60.112, 67.047, 70.082, 74.063,78.040,82.093, 87.028,95.038]
#R1 CD-2
#x = [3.024,6.112,10.017,14.048,17.049,21.001,29.109,33.031,36.100,40.067,45.117,49.102,54.090,58.029,61.094,65.067,75.095,82.008]
#R1 R-1
#x = [2.058,5.096,10.026,15.117,20.040,23.097,29.022, 33.049, 36.099,41.019, 46.083, 56.068, 60.106, 63.119, 69.007, 72.026,75.086,79.063,87.002,91.015,96.064]
#R2 CD-1
x = [2.013,6.026,10.080,18.079,21.052,25.006,28.092,32.043,45.065,49.076,57.007,70.035,74.037,80.070,83.058,87.020,89.113,94.003]
#R2 CD-2
#x = [9.070,13.056,18.026,21.040,25.110,32.040,38.036,41.040,44.095,48,51.101,55.054,58.071,62.087,65.086,70.006,79.006,83.108,87.085,90.045,97.010]
#R2 R-1
#x = [0.114,5.067,8.111,14.066,17.113,21.115,26.072,29.041,35.118,40.051,49.033,53.093,57.050,62.113,67,70.108,75.065,81.053,85.076,89.103,96.027,99.063]
#R2 R-2
#x = [1.012,4.112,9.113,14.048,20.101,24.043,27.076,30.102,35.012,39.057,43.014,47.056,61.015,64.108,68.008,70.029,78.050,86.002,90.085,95.017,104.002,107.051]
#R2 JL
#x = [2.020,5.081,9.059,14.004,16.115,19.100,22.049,27.056,31.040,34.077,39.025,43.076,48.119,52.119,59.057,63.097,67.103,78.003,82.099,86.084,90.059,93.114]
#R3 CD-1
#x = [3.106,6.081,15.009,17.049,19.028,23.019,27.117,31.100,37.022,41.057,45.068,50.015,61.072,65.044,68.089,72.022,75.078,79.022,82.101,93.037]
#R3-R
#x=[3.050,08.116,13.040,17.082,21.098,25.015,29.049,33.026,36.084,39.047,42.078,47.009,50.095,54.000,57.001,60.116,64.113,69.040,75.063,82.097,90.031]
#R4 CD 1
#x=[01.096,05.078,09.111,14.007,17.042,20.053,23.020,26.058,32.041,35.101,39.106,43.001,47.057,50.102,70.007,73.038,76.07,82.034,85.092,88.105,93.076]

##### On récupère l'index du temps de la frappe #####
index = [round(i/0.000625) for i in x]
print(index)

plt.plot(data['time_s'],data['ax_m/s/s'])
plt.xlabel('échantillons')
plt.ylabel('f(x)')
plt.title('R1-CD-1_TS-02092')
plt.show()

#### Création des dossiers
if not os.path.exists('Test/'+nom_fichier+'/CSV/ax'):
 os.makedirs('Test/'+nom_fichier+'/CSV/ax')
if not os.path.exists('Test/' + nom_fichier + '/CSV/ay'):
 os.makedirs('Test/' + nom_fichier + '/CSV/ay')
if not os.path.exists('Test/' + nom_fichier + '/CSV/az'):
 os.makedirs('Test/' + nom_fichier + '/CSV/az')



###Découpage et enregistrement au format CSV####
j = 0
for k in index:

    # On récupère la partie intéressante à +/- 2s
    t = data['time_s'].get([i for i in range(k-3200,k+3200)if data['time_s'].get(i)!= None])
    x = data['ax_m/s/s'].get([i for i in range(k-3200,k+3200) if data['ax_m/s/s'].get(i)!= None ])
    y = data['ay_m/s/s'].get([i for i in range(k-3200,k+3200)if data['ay_m/s/s'].get(i)!= None])
    z = data['az_m/s/s'].get([i for i in range(k-3200,k+3200)if data['az_m/s/s'].get(i)!= None])

    # Enregistrement au fomat CSV
    df_ax = pd.DataFrame({'ax': x, 't': t}, columns=['ax', 't'])
    df_ax.to_csv(dossier + nom_fichier + '/CSV/ax/' + 'découpage_ax_'+str(j)+'.csv')
    df_ax = pd.DataFrame({'ay': y, 't': t}, columns=['ay', 't'])
    df_ax.to_csv(dossier + nom_fichier + '/CSV/ay/' + 'découpage_ay_' + str(j) + '.csv')
    df_ax = pd.DataFrame({'az': z, 't': t}, columns=['az', 't'])
    df_ax.to_csv(dossier + nom_fichier + '/CSV/az/' + 'découpage_az_' + str(j) + '.csv')
    j += 1