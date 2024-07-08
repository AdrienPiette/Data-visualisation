import pandas as pd
import json
import csv
import numpy as np

df = pd.read_json('final_dataset.json')



#cleaning data

'''

- No duplicates
- No blank spaces (ex: `" I love python "` => `"I love python"`)
- No errors
- No empty values

'''
def cleaning ():

    df.dropna()
    df.fillna()
    df.drop_duplicates()

    return df

cleaning()

df_cleaned = cleaning()

print(df_cleaned)