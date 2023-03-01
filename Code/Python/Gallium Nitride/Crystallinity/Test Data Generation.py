# Andrew S. Messecar
# 2023

# Script for generating the testing data for a random forest algorithm that has been
# trained on GaN PAMBE synthesis data.

import csv

# Median Substrate Temperature = 550
# Median N2 Pressure = 0.00001
Gallium_Temperature = 960
Power = 350

header = ['Substrate Temperature', 'N2 Pressure', 'Ga Temperature', 'RF']

with open('Mapping_Data.csv', 'w', encoding='UTF8', newline='') as f:
   
   writer = csv.writer(f)
   writer.writerow(header)

   for i in range(1000):

      for j in range(20000):

           data = [1000 - i, j * (10**-9), Gallium_Temperature, Power]
       
           writer.writerow(data)
