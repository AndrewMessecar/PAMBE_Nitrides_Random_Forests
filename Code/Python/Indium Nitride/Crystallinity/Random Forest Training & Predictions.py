# Andrew S. Messecar
# 2023

# Script for training a random forest ensemble algorithm on InN PAMBE synthesis data and
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
Test_Inputs = pd.read_csv(r'# File Path of Test Data File')

Training_Data = pd.DataFrame(Epitaxy, columns=['Substrate Temperature','N2 Pressure', 'In Temperature', 'RF', 'Crystal'])

Map_Space = pd.DataFrame(Test_Inputs, columns=['Substrate Temperature', 'N2 Pressure', 'In Temperature', 'RF'])

Training_Inputs = Training_Data.loc[:, ['Substrate Temperature','N2 Pressure', 'In Temperature', 'RF']]

Training_Outputs = Training_Data.loc[:, 'Crystal']

scaler = MinMaxScaler() 
scaler.fit(Training_Inputs)
Training_Inputs = scaler.transform(Training_Inputs)
Map_Space = scaler.transform(Map_Space)

Predictor = RandomForestRegressor(max_features=5, random_state=42, n_estimators=245)

Predictor.fit(Training_Inputs, Training_Outputs)

Map = empty([850,3000])

Map = Predictor.predict(Map_Space)

figure(dpi=1200)
sb.heatmap(Map.reshape(850, 3000))

yticks(arange(-0.01, 850, step=50), ['850', '800', '750', '700', '650', '600', '550', '500', '450', '400', '350', '300', '250', '200', '150', '100', '50', '0'])

xticks(arange(-0.01, 3000, step=200), ['0' , '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30'],rotation=0)

title("Probability of InN Growing Single Crystalline")
xlabel("Initial Nitrogen Pressure (microtorr)")
ylabel("Effusion Cell Temperature (Celsius)")

show()
