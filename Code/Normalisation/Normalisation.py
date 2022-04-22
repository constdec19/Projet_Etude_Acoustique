import os
from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
import soundfile as sf


## CHANGER LES 2 LIENS ##
nom_fichier2 = 'C:/Users/Desktop/R1-CD-1_TS-02092_2021-05-07-18-28-19_aligned.csv'
nom_fichier = 'R1-CD-1_TS-02092_2021-05-07-18-28-19_aligned'
data = pd.read_csv(nom_fichier2)
print(data.shape)
print(data.columns)

##  CHANGER LE LIEN  ##  Création du dossier qui va être amené a contenir l'image#
if not os.path.exists('C:/Users/Desktop/'+nom_fichier):
 os.makedirs('C:/Users/Desktop/'+nom_fichier)

## DEBUT POUR AX ##
##-------------------------------------------------------------------------------------##

#Centré puis normalisé pour ax
y_ax = data['ax_m/s/s'] - mean(data['ax_m/s/s'])
y_ax_normalisé = y_ax / max([max(y_ax),abs(min(y_ax))])
y_ax_final = y_ax_normalisé

#Création dataframe avec nouvelles valeurs de ax
df_ax = pd.DataFrame({'ax': y_ax_final, 't': data['time_s']}, columns = ['ax', 't'])

#Juste pour affihcer le dataframe
print(df_ax)

##  CHANGER LE LIEN  ##  Sauvegarde du dataframe en fichier csv
df_ax.to_csv('C:/Users/Desktop/'+nom_fichier+'/'+nom_fichier+'_valeurs_normalisées_ax.csv')


#Juste pour afficher l'image
plt.plot(data['time_s'],y_ax_final)
plt.show()

##-------------------------------------------------------------------------------------##
## FIN POUR AX ##



## DEBUT POUR AY ##
##-------------------------------------------------------------------------------------##

#Centré puis normalisé pour ax
y_ay = data['ay_m/s/s'] - mean(data['ay_m/s/s'])
y_ay_normalisé = y_ay / max([max(y_ay),abs(min(y_ay))])
y_ay_final = y_ay_normalisé

#Création dataframe avec nouvelles valeurs de ax
df_ay = pd.DataFrame({'ay': y_ay_final, 't': data['time_s']}, columns = ['ay', 't'])

#Juste pour affihcer le dataframe
print(df_ay)

##  CHANGER LE LIEN  ##  Sauvegarde du dataframe en fichier csv
df_ay.to_csv('C:/Users/Desktop/'+nom_fichier+'/'+nom_fichier+'_valeurs_normalisées_ay.csv')

#Juste pour afficher l'image
plt.plot(data['time_s'],y_ay_final)
plt.show()


##-------------------------------------------------------------------------------------##
## FIN POUR AY ##


## DEBUT POUR AZ ##
##-------------------------------------------------------------------------------------##

#Centré puis normalisé pour ax
y_az = data['az_m/s/s'] - mean(data['az_m/s/s'])
y_az_normalisé = y_az / max([max(y_az),abs(min(y_az))])
y_az_final = y_az_normalisé

#Création dataframe avec nouvelles valeurs de ax
df_az = pd.DataFrame({'az': y_az_final, 't': data['time_s']}, columns = ['az', 't'])

#Juste pour affihcer le dataframe
print(df_az)

##  CHANGER LE LIEN  ##  Sauvegarde du dataframe en fichier csv
df_az.to_csv('C:/Users/Desktop/'+nom_fichier+'/'+nom_fichier+'_valeurs_normalisées_az.csv')

#Juste pour afficher l'image
plt.plot(data['time_s'],y_az_final)
plt.show()


##-------------------------------------------------------------------------------------##
## FIN POUR AZ ##

## CHANGER LE LIEN ## creation du wav #
df = pd.read_csv('C:/Users/Desktop/'+nom_fichier+'/'+nom_fichier+'_valeurs_normalisées_ax.csv')
times = df['t'].values
n_measurements = len(times)
timespan_seconds = times[-1] - times[0]
sample_rate_hz = int(n_measurements / timespan_seconds)
data = df['ax'].values
sf.write('C:/Users/Desktop/'+nom_fichier+'/son_x.wav', data, sample_rate_hz)


df = pd.read_csv('C:/Users/Desktop/'+nom_fichier+'/'+nom_fichier+'_valeurs_normalisées_ay.csv')
times = df['t'].values
n_measurements = len(times)
timespan_seconds = times[-1] - times[0]
sample_rate_hz = int(n_measurements / timespan_seconds)
data = df['ay'].values
sf.write('C:/Users/Desktop/'+nom_fichier+'/son_y.wav', data, sample_rate_hz)


df = pd.read_csv('C:/Users/Desktop/'+nom_fichier+'/'+nom_fichier+'_valeurs_normalisées_az.csv')
times = df['t'].values
n_measurements = len(times)
timespan_seconds = times[-1] - times[0]
sample_rate_hz = int(n_measurements / timespan_seconds)
data = df['az'].values
sf.write('C:/Users/Desktop/'+nom_fichier+'/son_z.wav', data, sample_rate_hz)