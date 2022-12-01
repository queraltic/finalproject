import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
import pickle
from PIL import Image
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt




st.title("Result")
st.write("""
        This result is based on the answers of the survey and the result of other countries.\n
        Example for a patient that has Binge Eating Disorder
        """) 
st.image("/Users/queraltiglesias/Desktop/pantallas.png", use_column_width=True)
