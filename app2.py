import streamlit as st 
import pandas as pd
import numpy as np
import os
from matplotlib import image
import plotly.express as px


st.set_page_config(layout='wide')
page=st.sidebar.selectbox("Pages",("Introduction","Visualization","Prediction"))

if page=="Introduction":
    st.title("Dashboard - Titanic Data Visualization")
    st.subheader("Authored by Ramesh Kori")
    st.write("On April 15, 1912, during her maiden voyage, the widely considered unsinkable"
          " RMS Titanic sank after colliding with an iceberg. Unfortunately, there were not"
           " enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.")


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

github="https://github.com/Ramesh-Kori"
var1=st.write("Github Link: {}".format(github))
    
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

#Pie Chart
var=st.selectbox("Pie Chart",("survived","class","sex","embarked"))
data=df[var].value_counts()
fig = px.pie(values=data.values, names=data.index)
st.plotly_chart(fig)
    
#Histogram Chart
var = st.selectbox("Histogram Chart",("age","sibsp","parch","fare"))
fig = px.histogram(data, x=df[var])
st.plotly_chart(fig)
    
#Bar Plot
var = st.selectbox("Bar Chart",("class","sex","embarked"))
data = df.groupby([var,"survived"])[["age"]].count().reset_index()
fig = px.bar(x=df[var], y=df["age"], color=df["survived"])
st.plotly_chart(fig)

    #Tree Map
data = df.groupby(["embarked","class","sex","survived"])[["fare"]].count().reset_index()
vars = st.multiselect('Choose Variable',["embarked","class","sex","survived"])
fig=px.treemap(df,path=vars,values='fare')
st.plotly_chart(fig)

col1, col2=st.columns(2)
    
var1,var2="class","age"
with col1:
    var1=st.selectbox("Box Plot",("class","sex"))
with col2:
    var2=st.selectbox("Box Plot",("age","fare"))
    
    #Box Plot
fig = px.box(df, x=var1, y=var2, color= "survived")
st.plotly_chart(fig)


