import matplotlib.pyplot as plt
import os
from statistics import mean,pstdev
from scipy import signal
import pandas as pd
import numpy as np

# axe dont l'on veut le fichier
axe = '/ax'

### 1er fichier

nom_fichier = 'R1-CD-1_TS-02092_2021-05-07-18-28-19_aligned'
nom_fichier2 = 'R1-CD-1_TS-02123_2021-05-07-18-28-19_aligned'
nom_fichier3 = 'R1-CD-1_TS-02134_2021-05-07-18-28-19_aligned'
nom_fichier4 = 'R4-R-1_TS-02134_2021-05-07-18-28-22_aligned'
dossier = 'Test/R1/CD-1/'
file = 'R1-CD-1'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)



val1 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val1.append(i)


for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val1.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val1.append(i)



### 2ème fichier

nom_fichier = 'R1-CD-2_TS-02092_2021-05-07-18-28-17_aligned'
nom_fichier2 = 'R1-CD-2_TS-02123_2021-05-07-18-28-17_aligned'
nom_fichier3 = 'R1-CD-2_TS-02134_2021-05-07-18-28-17_aligned'
nom_fichier4 = 'R4-R-1_TS-02134_2021-05-07-18-28-22_aligned'
dossier = 'Test/R1/CD-2/'
file = 'R1-CD-2'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)


val = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val.append(i)


for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val.append(i)



### 3ème fichier

nom_fichier = 'R1-R-1_TS-02092_2021-05-07-18-28-16_aligned'
nom_fichier2 = 'R1-R-1_TS-02123_2021-05-07-18-28-16_aligned'
nom_fichier3 = 'R1-R-1_TS-02131_2021-05-07-18-28-16_aligned'
nom_fichier4 = 'R1-R-1_TS-02134_2021-05-07-18-28-16_aligned'
dossier = 'Test/R1/R-1/'
file = 'R1-R-1'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)




val2 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val2.append(i)


for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val2.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val2.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
         val2.append(i)


### 4ème fichier

nom_fichier = 'R2-CD-1_TS-02092_2021-05-07-18-28-39_aligned'
nom_fichier2 = 'R2-CD-1_TS-02105_2021-05-07-18-28-39_aligned'
nom_fichier3 = 'R2-CD-1_TS-02123_2021-05-07-18-28-39_aligned'
nom_fichier4 = 'R2-CD-1_TS-02134_2021-05-07-18-28-39_aligned'
dossier = 'Test/R2/CD-1/'
file = 'R2-CD-1'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)



val3 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val3.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val3.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val3.append(i)

for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
         val3.append(i)


### 5ème fichier


nom_fichier = 'R2-CD-2_TS-02092_2021-05-07-18-28-37_aligned'
nom_fichier2 = 'R2-CD-2_TS-02105_2021-05-07-18-28-37_aligned'
nom_fichier3 = 'R2-CD-2_TS-02123_2021-05-07-18-28-37_aligned'
nom_fichier4 = 'R2-CD-2_TS-02134_2021-05-07-18-28-37_aligned'
dossier = 'Test/R2/CD-2/'
file = 'R2-CD-2'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)




val4 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val4.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val4.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val4.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
         val4.append(i)


### 6ème fichier


nom_fichier = 'R2-JL-1_TS-02092_2021-05-07-18-28-31_aligned'
nom_fichier2 = 'R2-JL-1_TS-02105_2021-05-07-18-28-31_aligned'
nom_fichier3 = 'R2-JL-1_TS-02123_2021-05-07-18-28-31_aligned'
nom_fichier4 = 'R2-JL-1_TS-02134_2021-05-07-18-28-31_aligned'
dossier = 'Test/R2/JL-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)




val5 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val5.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val5.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val5.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
         val5.append(i)


### 7ème fichier


nom_fichier = 'R2-R-1_TS-02092_2021-05-07-18-28-36_aligned'
nom_fichier2 = 'R2-R-1_TS-02105_2021-05-07-18-28-36_aligned'
nom_fichier3 = 'R2-R-1_TS-02123_2021-05-07-18-28-36_aligned'
nom_fichier4 = 'R2-R-1_TS-02134_2021-05-07-18-28-36_aligned'
dossier = 'Test/R2/R-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)




val6 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val6.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val6.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val6.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
         val6.append(i)


### 8ème fichier

nom_fichier = 'R2-R-2_TS-02092_2021-05-07-18-28-35_aligned'
nom_fichier2 = 'R2-R-2_TS-02105_2021-05-07-18-28-35_aligned'
nom_fichier3 = 'R2-R-2_TS-02123_2021-05-07-18-28-35_aligned'
nom_fichier4 = 'R2-R-2_TS-02134_2021-05-07-18-28-35_aligned'

dossier = 'Test/R2/R-2/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)



val7 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val7.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val7.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val7.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
         val7.append(i)


### 9ème fichier


nom_fichier = 'R3-CD-1_TS-02092_2021-05-07-18-28-13_aligned'
nom_fichier2 = 'R3-CD-1_TS-02123_2021-05-07-18-28-13_aligned'
nom_fichier3 = 'R3-CD-1_TS-02131_2021-05-07-18-28-13_aligned'
nom_fichier4 = 'R3-CD-1_TS-02134_2021-05-07-18-28-13_aligned'
dossier = 'Test/R3/CD-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)



val8 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val8.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val8.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val8.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
        val8.append(i)



### 10ème fichier

nom_fichier = 'R3-R-1_TS-02092_2021-05-07-18-28-12_aligned'
nom_fichier2 = 'R3-R-1_TS-02123_2021-05-07-18-28-12_aligned'
nom_fichier3 = 'R3-R-1_TS-02131_2021-05-07-18-28-12_aligned'
nom_fichier4 = 'R3-R-1_TS-02134_2021-05-07-18-28-12_aligned'
dossier = 'Test/R3/R-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)




val9 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val9.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val9.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val9.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
        val9.append(i)


### 11ème fichier


nom_fichier = 'R4-CD-1_TS-02092_2021-05-07-18-28-30_aligned'
nom_fichier2 = 'R4-CD-1_TS-02105_2021-05-07-18-28-30_aligned'
nom_fichier3 = 'R4-CD-1_TS-02123_2021-05-07-18-28-30_aligned'
nom_fichier4 = 'R4-CD-1_TS-02134_2021-05-07-18-28-30_aligned'
dossier = 'Test/R4/CD-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)


val10 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val10.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val10.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val10.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
        val10.append(i)



### 12ème fichier


nom_fichier = 'R4-CD-2_TS-02092_2021-05-07-18-28-25_aligned'
nom_fichier2 = 'R4-CD-2_TS-02105_2021-05-07-18-28-25_aligned'
nom_fichier3 = 'R4-CD-2_TS-02123_2021-05-07-18-28-25_aligned'
nom_fichier4 = 'R4-CD-2_TS-02134_2021-05-07-18-28-25_aligned'
dossier = 'Test/R4/CD-2/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)



val11 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val11.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val11.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val11.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
        val11.append(i)


### 13ème fichier



nom_fichier = 'R4-R-1_TS-02092_2021-05-07-18-28-22_aligned'
nom_fichier2 = 'R4-R-1_TS-02105_2021-05-07-18-28-22_aligned'
nom_fichier3 = 'R4-R-1_TS-02123_2021-05-07-18-28-22_aligned'
nom_fichier4 = 'R4-R-1_TS-02134_2021-05-07-18-28-22_aligned'
dossier = 'Test/R4/R-1/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)
list4 = os.listdir(dossier+nom_fichier4+'/Centroid' + axe)



val12 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val12.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val12.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val12.append(i)
for i in list4:
     data_x = pd.read_csv(dossier + nom_fichier4 + '/Centroid'+axe+'/'+i)
     for i in data_x['centroid']:
        val12.append(i)



### 14ème fichier


nom_fichier = 'R4-R-2_TS-02092_2021-05-07-18-28-21_aligned'
nom_fichier2 = 'R4-R-2_TS-02123_2021-05-07-18-28-21_aligned'
nom_fichier3 = 'R4-R-2_TS-02134_2021-05-07-18-28-21_aligned'
dossier = 'Test/R4/R-2/'

### Récupère les noms des fichiers en .csv
list1 = os.listdir(dossier+nom_fichier+'/Centroid'+axe)
list2 = os.listdir(dossier+nom_fichier2+'/Centroid'+ axe)
list3 = os.listdir(dossier+nom_fichier3+'/Centroid'+ axe)



val13 = []
for i in list1:
    data_x = pd.read_csv(dossier+nom_fichier+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val13.append(i)

for i in list2:
    data_x = pd.read_csv(dossier+nom_fichier2+'/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val13.append(i)


for i in list3:
    data_x = pd.read_csv(dossier + nom_fichier3 + '/Centroid'+axe+'/'+i)
    for i in data_x['centroid']:
        val13.append(i)



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


# Enregistrer au format CSV
df_ax = pd.DataFrame({'R1-CD1':val1,'R1-CD2': val,'R1-R1':val2,'R2-CD1':val3,'R2-CD2':val4,'R2-JL':val5,'R2-R1':val6,'R2-R2':val7,'R3-CD':val8,'R3-R':val9,'R4-CD1':val10,'R4-CD2':val11,'R4-R1':val12,'R4-R2':val13}, columns=['R1-CD1','R1-CD2','R1-R1','R2-CD1','R2-CD2','R2-JL','R2-R1','R2-R2','R3-CD','R3-R','R4-CD1','R4-CD2','R4-R1','R4-R2'])
df_ax.to_csv('Test/centroid_z.csv',index = False)