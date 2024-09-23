import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

# import os
# os.getcwd()
# print(os.getcwd())

st.title('California Housing Data(1990) by Hairong Zheng')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Median House Price:', 0, 500001, 200000)

capital_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults



income_filter = st.sidebar.radio('Choose income level', 
                          ('Low','Median','High'))

df=df[df.median_house_value<= price_filter]

if  income_filter=='Low':
      df=df[df.median_income<=2.5]
if  income_filter=='Medium':
      df=df[(df.median_income>2.5)&(df.median_income<4.5)]                                             
if  income_filter=='High':
      df=df[df.median_income>=4.5]

st.subheader('See more filters in the sidebar')
st.map(df)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 10))
df.median_house_value.plot.hist(ax=ax,bins=30)
st.pyplot(fig)
