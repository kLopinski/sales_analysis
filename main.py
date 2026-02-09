import pandas as pd
import numpy as np
import os
print(os.getcwd())
#loading data
data = pd.read_csv("data/Online_Retail.csv", encoding='ISO-8859-1')

#cleaning data
# - CustomerID: missing, but it isnt required analysis
# - Description: missing but it isnt required for analysis
# - Conclusion: Leaving rows with nan values due to the lack of their significance for this analysis

data.info()
#Counting missing columns
print(data.isna().sum())
#Checking for importance 
print(data["Description"].head())


#Checking for possible anomalies
print((data['Quantity'] <= 0).sum())
print((data['UnitPrice'] <= 0).sum())

#Considering the description high possibility of discounts and refunds
anomalous_data = data[(data["UnitPrice"] <= 0) | (data['Quantity'] <= 0)]

print(anomalous_data.head(10))