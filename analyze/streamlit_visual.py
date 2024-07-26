import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import plotly.express as px


df_sales = pd.read_csv('df_cleaned_sale.csv')

st.title('Data Analysis')
st.write('This is the data analysis page. Here you can explore the data and see some visualizations.')  
st.write('first, let us see the data we are working with')
st.dataframe(df_sales.head())
st.dataframe(df_sales.describe())


st.write('Now, let us see the distribution of the sales prices')


df_filtered = df_sales[df_sales['Price'] < 800000]
df_average_price = df_filtered['Price'].median()

st.write(f'The median price of the sales is €{df_average_price:.2f}')
st.write('Below is the distribution of the prices')


plt.figure(figsize=(12, 8))
px.histogram(df_filtered['Price'], kde=True) 
plt.title('Distribution of Prices')
plt.xlabel('Prices (€)')
plt.ylabel('Frequency')
plt.axvline(df_average_price, color='r', linestyle='--', linewidth=2, label=f'Median Price: €{df_average_price:.2f}')  
plt.legend()


st.plotly_chart(px.histogram(df_filtered['Price'], kde=True))
