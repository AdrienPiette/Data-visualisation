import pandas as pd
import json
import csv
import numpy as np




df = pd.read_json("final_dataset.json")


print(df.head())
print(df)




























'''#cleaning data



- No duplicates
- No blank spaces (ex: `" I love python "` => `"I love python"`)
- No errors
- No empty values




df.dropna()
df.fillna()
df.drop_duplicates()

#data analysing



- How many rows and columns?
- What is the correlation between the variables and the price? (Why might that be?)
- How are variables correlated to each other? (Why?)
- Which variables have the greatest influence on the price?
- Which variables have the least influence on the price?
- How many qualitative and quantitative variables are there? How would you transform these values into numerical values?



df.shape()
df.info()
df.columns.tolist()
df.describe()
df.columns.tolist()
df.max()
df.isnull().sum()


#data visualization'''







