import matplotlib.pyplot as plt
import os
from statistics import mean,pstdev
from scipy import signal
import pandas as pd
import numpy as np
import math

# A changer en fonction de l'axe que l'on veut
axe = '/ax'
vdb = 'Vdbx'


### 1er fichier

nom_fichier = 'R1-CD-1_TS-02092_2021-05-07-18-28-19_aligned'
nom_fichier2 = 'R1-CD-1_TS-02123_2021-05-07-18-28-19_aligned'
nom_fichier3 = 'R1-CD-1_TS-02134_2021-05-07-18-28-19_aligned'
nom_fichier4 = 'R4-R-1_TS-02134_2021-05-07-18-28-22_aligned'
dossier = 'Test/R1/CD-1/'
file = 'R1-CD-1'


### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)

val1 = []
max1 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/NVibratoire'+axe+'/'+i)

    if (mean(data_x[vdb])!= -math.inf) :
        val1.append(mean(data_x[vdb]))

    max1.append(max(data_x[vdb]))


for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/NVibratoire'+axe+'/'+i)
    if (mean(data_x[vdb]) != -math.inf):
        val1.append(mean(data_x[vdb]))

    max1.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire'+axe+'/'+i)
    if (mean(data_x[vdb]) != -math.inf):
        val1.append(mean(data_x[vdb]))

    max1.append(max(data_x[vdb]))



### 2ème fichier

nom_fichier = 'R1-CD-2_TS-02092_2021-05-07-18-28-17_aligned'
nom_fichier2 = 'R1-CD-2_TS-02123_2021-05-07-18-28-17_aligned'
nom_fichier3 = 'R1-CD-2_TS-02134_2021-05-07-18-28-17_aligned'
nom_fichier4 = 'R4-R-1_TS-02134_2021-05-07-18-28-22_aligned'
dossier = 'Test/R1/CD-2/'
file = 'R1-CD-2'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)




val = []
max0 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val.append(mean(data_x[vdb]))

    max0.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val.append(mean(data_x[vdb]))

    max0.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val.append(mean(data_x[vdb]))

    max0.append(max(data_x[vdb]))


### 3ème fichier

nom_fichier = 'R1-R-1_TS-02092_2021-05-07-18-28-16_aligned'
nom_fichier2 = 'R1-R-1_TS-02123_2021-05-07-18-28-16_aligned'
nom_fichier3 = 'R1-R-1_TS-02131_2021-05-07-18-28-16_aligned'
nom_fichier4 = 'R1-R-1_TS-02134_2021-05-07-18-28-16_aligned'
dossier = 'Test/R1/R-1/'
file = 'R1-R-1'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)


val2 = []
max2 =  []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val2.append(mean(data_x[vdb]))

    max2.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val2.append(mean(data_x[vdb]))

    max2.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val2.append(mean(data_x[vdb]))

    max2.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val2.append(mean(data_x[vdb]))

     max2.append(max(data_x[vdb]))


### 4ème fichier

nom_fichier = 'R2-CD-1_TS-02092_2021-05-07-18-28-39_aligned'
nom_fichier2 = 'R2-CD-1_TS-02105_2021-05-07-18-28-39_aligned'
nom_fichier3 = 'R2-CD-1_TS-02123_2021-05-07-18-28-39_aligned'
nom_fichier4 = 'R2-CD-1_TS-02134_2021-05-07-18-28-39_aligned'
dossier = 'Test/R2/CD-1/'
file = 'R2-CD-1'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)



val3 = []
max3 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val3.append(mean(data_x[vdb]))

    max3.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val3.append(mean(data_x[vdb]))

    max3.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val3.append(mean(data_x[vdb]))

    max3.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val3.append(mean(data_x[vdb]))

     max3.append(max(data_x[vdb]))


### 5ème fichier

nom_fichier = 'R2-CD-2_TS-02092_2021-05-07-18-28-37_aligned'
nom_fichier2 = 'R2-CD-2_TS-02105_2021-05-07-18-28-37_aligned'
nom_fichier3 = 'R2-CD-2_TS-02123_2021-05-07-18-28-37_aligned'
nom_fichier4 = 'R2-CD-2_TS-02134_2021-05-07-18-28-37_aligned'
dossier = 'Test/R2/CD-2/'
file = 'R2-CD-2'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)


val4 = []
max4 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val4.append(mean(data_x[vdb]))

    max4.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val4.append(mean(data_x[vdb]))

    max4.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val4.append(mean(data_x[vdb]))

    max4.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val4.append(mean(data_x[vdb]))

     max4.append(max(data_x[vdb]))

### 6ème fichier

nom_fichier = 'R2-JL-1_TS-02092_2021-05-07-18-28-31_aligned'
nom_fichier2 = 'R2-JL-1_TS-02105_2021-05-07-18-28-31_aligned'
nom_fichier3 = 'R2-JL-1_TS-02123_2021-05-07-18-28-31_aligned'
nom_fichier4 = 'R2-JL-1_TS-02134_2021-05-07-18-28-31_aligned'
dossier = 'Test/R2/JL-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)


val5 = []
max5 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val5.append(mean(data_x[vdb]))

    max5.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val5.append(mean(data_x[vdb]))

    max5.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val5.append(mean(data_x[vdb]))

    max5.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val5.append(mean(data_x[vdb]))

     max5.append(max(data_x[vdb]))

### 7ème fichier

nom_fichier = 'R2-R-1_TS-02092_2021-05-07-18-28-36_aligned'
nom_fichier2 = 'R2-R-1_TS-02105_2021-05-07-18-28-36_aligned'
nom_fichier3 = 'R2-R-1_TS-02123_2021-05-07-18-28-36_aligned'
nom_fichier4 = 'R2-R-1_TS-02134_2021-05-07-18-28-36_aligned'
dossier = 'Test/R2/R-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)


val6 = []
max6 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val6.append(mean(data_x[vdb]))

    max6.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val6.append(mean(data_x[vdb]))

    max6.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val6.append(mean(data_x[vdb]))

    max6.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val6.append(mean(data_x[vdb]))

     max6.append(max(data_x[vdb]))

### 8ème fichier

nom_fichier = 'R2-R-2_TS-02092_2021-05-07-18-28-35_aligned'
nom_fichier2 = 'R2-R-2_TS-02105_2021-05-07-18-28-35_aligned'
nom_fichier3 = 'R2-R-2_TS-02123_2021-05-07-18-28-35_aligned'
nom_fichier4 = 'R2-R-2_TS-02134_2021-05-07-18-28-35_aligned'

dossier = 'Test/R2/R-2/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)


val7 = []
max7 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val7.append(mean(data_x[vdb]))

    max7.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val7.append(mean(data_x[vdb]))

    max7.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val7.append(mean(data_x[vdb]))

    max7.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val7.append(mean(data_x[vdb]))

     max7.append(max(data_x[vdb]))

### 9ème fichier

nom_fichier = 'R3-CD-1_TS-02092_2021-05-07-18-28-13_aligned'
nom_fichier2 = 'R3-CD-1_TS-02123_2021-05-07-18-28-13_aligned'
nom_fichier3 = 'R3-CD-1_TS-02131_2021-05-07-18-28-13_aligned'
nom_fichier4 = 'R3-CD-1_TS-02134_2021-05-07-18-28-13_aligned'
dossier = 'Test/R3/CD-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)


val8 = []
max8 =[]
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val8.append(mean(data_x[vdb]))

    max8.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val8.append(mean(data_x[vdb]))

    max8.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val8.append(mean(data_x[vdb]))

    max8.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val8.append(mean(data_x[vdb]))

     max8.append(max(data_x[vdb]))



### 10ème fichier

nom_fichier = 'R3-R-1_TS-02092_2021-05-07-18-28-12_aligned'
nom_fichier2 = 'R3-R-1_TS-02123_2021-05-07-18-28-12_aligned'
nom_fichier3 = 'R3-R-1_TS-02131_2021-05-07-18-28-12_aligned'
nom_fichier4 = 'R3-R-1_TS-02134_2021-05-07-18-28-12_aligned'
dossier = 'Test/R3/R-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)


val9 = []
max9 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val9.append(mean(data_x[vdb]))

    max9.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val9.append(mean(data_x[vdb]))

    max9.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val9.append(mean(data_x[vdb]))

    max7.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val9.append(mean(data_x[vdb]))

     max9.append(max(data_x[vdb]))

### 11ème fichier

nom_fichier = 'R4-CD-1_TS-02092_2021-05-07-18-28-30_aligned'
nom_fichier2 = 'R4-CD-1_TS-02105_2021-05-07-18-28-30_aligned'
nom_fichier3 = 'R4-CD-1_TS-02123_2021-05-07-18-28-30_aligned'
nom_fichier4 = 'R4-CD-1_TS-02134_2021-05-07-18-28-30_aligned'
dossier = 'Test/R4/CD-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)



val10 = []
max10 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val10.append(mean(data_x[vdb]))

    max10.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val10.append(mean(data_x[vdb]))

    max10.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val10.append(mean(data_x[vdb]))

    max10.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val10.append(mean(data_x[vdb]))

     max10.append(max(data_x[vdb]))


### 12ème fichier

nom_fichier = 'R4-CD-2_TS-02092_2021-05-07-18-28-25_aligned'
nom_fichier2 = 'R4-CD-2_TS-02105_2021-05-07-18-28-25_aligned'
nom_fichier3 = 'R4-CD-2_TS-02123_2021-05-07-18-28-25_aligned'
nom_fichier4 = 'R4-CD-2_TS-02134_2021-05-07-18-28-25_aligned'
dossier = 'Test/R4/CD-2/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)


val11 = []
max11 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val11.append(mean(data_x[vdb]))

    max11.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val11.append(mean(data_x[vdb]))

    max11.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val11.append(mean(data_x[vdb]))

    max11.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val11.append(mean(data_x[vdb]))

     max11.append(max(data_x[vdb]))

### 13ème fichier

nom_fichier = 'R4-R-1_TS-02092_2021-05-07-18-28-22_aligned'
nom_fichier2 = 'R4-R-1_TS-02105_2021-05-07-18-28-22_aligned'
nom_fichier3 = 'R4-R-1_TS-02123_2021-05-07-18-28-22_aligned'
nom_fichier4 = 'R4-R-1_TS-02134_2021-05-07-18-28-22_aligned'
dossier = 'Test/R4/R-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/NVibratoire' + axe)


val12 = []
max12 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val12.append(mean(data_x[vdb]))

    max12.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val7.append(mean(data_x[vdb]))

    max7.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val12.append(mean(data_x[vdb]))

    max12.append(max(data_x[vdb]))
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/NVibratoire'+axe+'/'+i)
     if (mean(data_x[vdb]) != -math.inf):
         val12.append(mean(data_x[vdb]))

     max12.append(max(data_x[vdb]))

### 14ème fichier

nom_fichier = 'R4-R-2_TS-02092_2021-05-07-18-28-21_aligned'
nom_fichier2 = 'R4-R-2_TS-02123_2021-05-07-18-28-21_aligned'
nom_fichier3 = 'R4-R-2_TS-02134_2021-05-07-18-28-21_aligned'
dossier = 'Test/R4/R-2/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/NVibratoire'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/NVibratoire'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/NVibratoire'+ axe)





val13 = []
max13 = []
for i in list1:
    data_x = pd.read_csv(dossier + nom_fichier + '/NVibratoire' + axe + '/' + i)

    if (mean(data_x[vdb]) != -math.inf):
        val7.append(mean(data_x[vdb]))

    max13.append(max(data_x[vdb]))

for i in list2:
    data_x = pd.read_csv(dossier + nom_fichier2 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val13.append(mean(data_x[vdb]))

    max13.append(max(data_x[vdb]))

for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/NVibratoire' + axe + '/' + i)
    if (mean(data_x[vdb]) != -math.inf):
        val13.append(mean(data_x[vdb]))

    max13.append(max(data_x[vdb]))

## On met toutes les listes a la même longeur pour les enregistrer


maximum = max(len(val),len(val1),len(val2),len(val3),len(val4),len(val5),len(val6),len(val7),len(val8),len(val9),len(val10),len(val11),len(val12),len(val13))

if (len(val)!=maximum):
    nb = maximum - len(val)
    for j in range (nb):
        val.append(0)

if (len(val1)!=maximum):
    nb = maximum - len(val1)
    for j in range (nb):
        val1.append(0)
if (len(val2)!=maximum):
    nb = maximum - len(val2)
    for j in range (nb):
        val2.append(0)
if (len(val3)!=maximum):
    nb = maximum - len(val3)
    for j in range (nb):
        val3.append(0)
if (len(val4)!=maximum):
    nb = maximum - len(val4)
    for j in range (nb):
        val4.append(0)
if (len(val5)!=maximum):
    nb = maximum - len(val5)
    for j in range (nb):
        val5.append(0)
if (len(val6)!=maximum):
    nb = maximum - len(val6)
    for j in range (nb):
        val6.append(0)
if (len(val7)!=maximum):
    nb = maximum - len(val7)
    for j in range (nb):
        val7.append(0)
if (len(val8)!=maximum):
    nb = maximum - len(val8)
    for j in range (nb):
        val8.append(0)
if (len(val9)!=maximum):
    nb = maximum - len(val9)
    for j in range (nb):
        val9.append(0)
if (len(val10)!=maximum):
    nb = maximum - len(val10)
    for j in range (nb):
        val10.append(0)
if (len(val11)!=maximum):
    nb = maximum - len(val11)
    for j in range (nb):
        val11.append(0)
if (len(val12)!=maximum):
    nb = maximum - len(val12)
    for j in range (nb):
        val12.append(0)
if (len(val13)!=maximum):
    nb = maximum - len(val13)
    for j in range (nb):
        val13.append(0)



maximum = max(len(max0),len(max1),len(max2),len(max3),len(max4),len(max5),len(max6),len(max7),len(max8),len(max9),len(max10),len(max11),len(max12),len(max13))

if (len(max0)!=maximum):
    nb = maximum - len(max0)
    for j in range (nb):
        max0.append(0)

if (len(max1)!=maximum):
    nb = maximum - len(max1)
    for j in range (nb):
        max1.append(0)
if (len(max2)!=maximum):
    nb = maximum - len(max2)
    for j in range (nb):
        max2.append(0)
if (len(max3)!=maximum):
    nb = maximum - len(max3)
    for j in range (nb):
        max3.append(0)
if (len(max4)!=maximum):
    nb = maximum - len(max4)
    for j in range (nb):
        max4.append(0)
if (len(max5)!=maximum):
    nb = maximum - len(max5)
    for j in range (nb):
        max5.append(0)
if (len(max6)!=maximum):
    nb = maximum - len(max6)
    for j in range (nb):
        max6.append(0)
if (len(max7)!=maximum):
    nb = maximum - len(max7)
    for j in range (nb):
        max7.append(0)
if (len(max8)!=maximum):
    nb = maximum - len(max8)
    for j in range (nb):
        max8.append(0)
if (len(max9)!=maximum):
    nb = maximum - len(max9)
    for j in range (nb):
        max9.append(0)
if (len(max10)!=maximum):
    nb = maximum - len(max10)
    for j in range (nb):
        max10.append(0)
if (len(max11)!=maximum):
    nb = maximum - len(max11)
    for j in range (nb):
        max11.append(0)
if (len(max12)!=maximum):
    nb = maximum - len(max12)
    for j in range (nb):
        max12.append(0)
if (len(max13)!=maximum):
    nb = maximum - len(max13)
    for j in range (nb):
        max13.append(0)



# Enregistrer au format CSV

df_ax = pd.DataFrame({'R1-CD1':val1,'R1-CD2': val,'R1-R1':val2,'R2-CD1':val3,'R2-CD2':val4,'R2-JL':val5,'R2-R1':val6,'R2-R2':val7,'R3-CD':val8,'R3-R':val9,'R4-CD1':val10,'R4-CD2':val11,'R4-R1':val12,'R4-R2':val13}, columns=['R1-CD1','R1-CD2','R1-R1','R2-CD1','R2-CD2','R2-JL','R2-R1','R2-R2','R3-CD','R3-R','R4-CD1','R4-CD2','R4-R1','R4-R2'])
df_ax.to_csv('Test/Nvib_moy_x.csv',index = False)

df_ax = pd.DataFrame({'R1-CD1':max1,'R1-CD2': max0,'R1-R1':max2,'R2-CD1':max3,'R2-CD2':max4,'R2-JL':max5,'R2-R1':max6,'R2-R2':max7,'R3-CD':max8,'R3-R':max9,'R4-CD1':max10,'R4-CD2':max11,'R4-R1':max12,'R4-R2':max13}, columns=['R1-CD1','R1-CD2','R1-R1','R2-CD1','R2-CD2','R2-JL','R2-R1','R2-R2','R3-CD','R3-R','R4-CD1','R4-CD2','R4-R1','R4-R2'])
df_ax.to_csv('Test/Nvib_max_x.csv',index = False)