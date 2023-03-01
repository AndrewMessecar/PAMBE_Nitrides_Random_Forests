# Andrew S. Messecar
# 2023

# Script for generating the testing data for a random forest algorithm that has been
# trained on InN PAMBE synthesis data.

import csv

Substrate_Temperature = 450
# Median N2 Pressure = 0.00001
# Median Indium Temperature = 780
Power = 250

header = ['Substrate Temperature', 'N2 Pressure', 'In Temperature', 'RF']

with open('Mapping_Data.csv', 'w', encoding='UTF8', newline='') as f:

   writer = csv.writer(f)
   writer.writerow(header)

   for i in range(850):

      for j in range(3000):

           data = [Substrate_Temperature, j * (10**-8) + (10**-8), 850 - i, Power]
       
           writer.writerow(data)
