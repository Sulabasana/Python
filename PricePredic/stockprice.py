import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout , LSTR


# Load Data
company = 'FB'

# What data frame
start = dt.datetime(2012,1,1)
end = dt.datetime(2023,5,14)

data = web.DateReader(company, 'yahoo', start, end)

#Prepare Data

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform()
