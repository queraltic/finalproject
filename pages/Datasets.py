import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
import pickle
from PIL import Image
import seaborn as sns
import plotly.express as px


df = pd.read_csv ('/Users/queraltiglesias/Desktop/FINALPROJECT/finalproject/data/FinalProject.csv')
df1 = pd.read_csv ('/Users/queraltiglesias/Desktop/FINALPROJECT/finalproject/data/FinalProject2.csv')
df3 = pd.read_csv ('/Users/queraltiglesias/Desktop/FINALPROJECT/finalproject/data/FinalProject3.csv')

st.title("Dataset")
st.subheader("Survey") 
st.write(df)

st.subheader("App use")
st.write(df3)