# Andrew S. Messecar
import csv

# Median Substrate Temperature = 770
N2_Pressure = 0.00001
Gallium_Temperature = 960
# Median RF Power = 150
# Median Growth Time = 180

header = ['Substrate Temperature', 'RF Power', 'Ga Temperature', 'N2 Pressure']

with open('/home/garibasen/Documents/Data/WMU/Dropbox/S-squared/Mapping Data/Mapping_Data_Median.csv', 'w', encoding='UTF8', newline='') as f:
   writer = csv.writer(f)
   writer.writerow(header)

   for i in range(550):

      for j in range(1000):

           data = [j, 550 - i, Gallium_Temperature, N2_Pressure]
       
           writer.writerow(data)