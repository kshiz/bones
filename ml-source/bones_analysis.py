import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_excel('data/doctors.xlsx')

# Dropping the first row which contains all NaN data
dataset = dataset.drop([0])
dataset = dataset.drop([1])

dataset = dataset.rename(columns={
                          'Type': 'Row Labels', 
                          'TRUE': 'Count of Doctors',
                          'Unnamed: 2': 'Centers',
                          'Unnamed: 3': 'Population',
                          'Unnamed: 4': 'Areas',
                          'Unnamed: 5': 'Zones',
                          })

# Filling up NaN Values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'nan', strategy = 'mean', axis = 0)

# Label Encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()

