import pandas as pd
import numpy as np
import os
print(os.getcwd())

data = pd.read_csv("data/Online_Retail.csv", encoding='ISO-8859-1')

data.ino()
print(data.isna().sum())
print(data["Description"].head())
print((data['Quantity'] <= 0).sum())
print((data['UnitPrice'] <= 0).sum())

anomalous_data = data[(data["UnitPrice"] <= 0) | (data['Quantity'] <= 0)]

print(anomalous_data.head(10))
