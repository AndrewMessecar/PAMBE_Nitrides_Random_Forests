# Andrew S. Messecar
# 2023

# Script for training a random forest ensemble algorithm on GaN PAMBE synthesis data and
# using it to make predictions across an entire processing space (see "Mapping Data - GaN S2 - RF Plasma Power vs Substrate Temperature.py").

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from numpy import array, empty, reshape, arange
import pandas as pd
import seaborn as sb
from pylab import title, show, xlabel, ylabel, savefig, figure, yticks, xticks

# Import the training data
Epitaxy = pd.read_csv(r'# File Path of Training Data File')

# Import the test data for predictions (see "Mapping Data - GaN S2 - RF Plasma Power vs Substrate Temperature.py" file)
Test_Inputs = pd.read_csv(r'# File Path of Test Data File')')

Training_Data = pd.DataFrame(Epitaxy, columns=['Substrate Temperature', 'RF Power', 'Ga Temperature', 'N2 Pressure', 'S2'])

Map_Space = pd.DataFrame(Test_Inputs, columns=['Substrate Temperature', 'RF Power', 'Ga Temperature', 'N2 Pressure'])

Training_Inputs = Training_Data.loc[:, ['Substrate Temperature', 'RF Power', 'Ga Temperature', 'N2 Pressure']]

Training_Outputs = Training_Data.loc[:, 'S2']

scaler = MinMaxScaler() 
scaler.fit(Training_Inputs)
Training_Inputs = scaler.transform(Training_Inputs)
Map_Space = scaler.transform(Map_Space)

Predictor = RandomForestRegressor(max_features=5, random_state=42, n_estimators=245)

Predictor.fit(Training_Inputs, Training_Outputs)

Map = Predictor.predict(Map_Space)

figure(dpi=1200)
sb.heatmap(Map.reshape(550, 1000))
yticks(arange(-0.01, 550, step=50), ['550', '500', '450', '400', '350', '300', '250', '200', '150', '100', '50', '0'])
xticks(arange(-0.01, 1000, step=100), ['0' , '100', '200', '300', '400', '500', '600', '700', '800', '900', '1000'],rotation=0)
# title("Predicted S^2 in GaN Thin Film Crystal")
xlabel("Substrate Temperature (Celsius)")
ylabel("Plasma Source Power (Watts)")

show()
