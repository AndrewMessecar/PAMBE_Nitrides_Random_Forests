# Andrew S. Messecar
# 2023

# Script for training a random forest ensemble algorithm on GaN PAMBE synthesis data and
# using it to make predictions across an entire processing space (see "Test Data Generation.py").

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from numpy import array, empty, reshape, arange
import pandas as pd
import seaborn as sb
from pylab import title, show, xlabel, ylabel, savefig, figure, yticks, xticks

# Import the training data
Epitaxy = pd.read_csv(r'# File Path of Training Data File')

# Import the test data for predictions (see "Test Data Generation.py" file)
Test_Inputs = pd.read_csv(r'# File Path of Test Data File')')

Training_Data = pd.DataFrame(Epitaxy, columns=['Substrate Temperature', 'Ga Temperature', 'N2 Pressure', 'N2 Power', 'S-squared'])

Map_Space = pd.DataFrame(Test_Inputs, columns=['Substrate Temperature', 'Ga Temperature', 'N2 Pressure', 'N2 Power'])

Training_Inputs = Training_Data.loc[:, ['Substrate Temperature', 'Ga Temperature', 'N2 Pressure', 'N2 Power']]

Training_Outputs = Training_Data.loc[:, 'S-squared']

scaler = MinMaxScaler() 
scaler.fit(Training_Inputs)
Training_Inputs = scaler.transform(Training_Inputs)
Map_Space = scaler.transform(Map_Space)

Predictor = RandomForestRegressor(max_features=5, random_state=42, n_estimators=245)

Predictor.fit(Training_Inputs, Training_Outputs)

Map = empty([1000,20000])

Map = Predictor.predict(Map_Space)

figure(dpi=1200)
sb.heatmap(Map.reshape(1000, 20000))

yticks(arange(-0.01, 1000, step=100), ['1000', '900', '800', '700', '600', '500', '400', '300', '200', '100', '0'])

xticks(arange(-0.01, 20000, step=2000), ['0' , '2', '4', '6', '8', '10', '12', '14', '16', '18', '20'],rotation=0)

title("Predicted Bragg-Williams S^2 in GaN")
xlabel("Initial Nitrogen Pressure (microtorr)")
ylabel("Substrate Temperature (Celsius)")

show()
