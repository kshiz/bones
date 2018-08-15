import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_excel('data/doctors.xlsx')

# Dropping the first row which contains all NaN data
dataset = dataset.drop(dataset.index[[0,2]])

dataset = dataset.rename(columns=
                         {'Type': 'Row Labels', 
                          'TRUE': 'Count of Doctors',
                          'Unnamed: 2': 'Centers',
                          'Unnamed: 3': 'Population',
                          'Unnamed: 4': 'Areas',
                          'Unnamed: 5': 'Zones',
                          })