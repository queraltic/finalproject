import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
import pickle
from PIL import Image
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


df = pd.read_csv ('/Users/queraltiglesias/Desktop/FINALPROJECT/finalproject/data/FinalProject.csv')
df1 = pd.read_csv ('/Users/queraltiglesias/Desktop/FINALPROJECT/finalproject/data/FinalProject2.csv')
df3 = pd.read_csv ('/Users/queraltiglesias/Desktop/FINALPROJECT/finalproject/data/FinalProject3.csv')


st.set_page_config(
     page_title="Rise App",
     page_icon="",
     layout="wide",
)


# Title
st.title("Rise App: The app for improving the life of people with eating disorders ")
st.subheader("Why this project?")
st.write("""
        This project, is born like most of the apps from the needs of the people; in this case in having an app that's useful to help people here in spain who suffer from eating disorders.
        """) 
st.image("/Users/queraltiglesias/Desktop/FINALPROJECT/finalproject/images/FoodAnxiety-1024x819.jpg", use_column_width=True)







#figure
#figure= df1 = px.data.tips()
#fig = px.bar(df, x="Edad/Age:", y="Sexo/Sex", color="Paciente o especialista en salud mental/ patient or mental health specialist", barmode="group")
#plt.title("Count of days without binge eating?")
#plt.savefig("Count of days without binge eating?")
#st.plotly_chart(fig, use_container_width=True)
#figure1
#fig1 = plt.figure(figsize=(5, 4))
#sns.countplot(data=df, x= 'Has usado alguna app recomendada por un especialista en salud mental?/Have you used an app recommended by a mental health specialist?')
#plt.title("Have you used an app recommended by a mental health specialist?")
#st.pyplot(fig1)

#figure2
#fig2 = plt.figure(figsize=(4, 3))
#sns.countplot(data=df, x= '¿Días sin atracones?/Count of days without binge eating?')
#dtype={'caption' : str}
#plt.title("Count of days without binge eating?")
#st.pyplot(fig2)

#figure3
#fig3 = plt.figure(figsize=(4, 3))
#sns.countplot(data=df, x= df.columns[8])
#dtype={'caption' : str}
#plt.title("Motivational Quote")
#st.pyplot(fig3)

#figure4
#fig4 = plt.figure(figsize=(4, 3))
#sns.countplot(data=df, x= '¿Apuntar comidas de cada dia?/Record daily meals?')
#dtype={'caption' : str}
#plt.title("Record daily meals?")
#st.pyplot(fig4)

#figure5
#fig5 = plt.figure(figsize=(4, 3))
#sns.countplot(data=df, x= df.columns[11])
#dtype={'caption' : str}
#plt.title("List of helpful strategies?")
#st.pyplot(fig5)

#figure6
#fig6 = plt.figure(figsize=(4, 3))
#sns.countplot(data=df, x="¿Botón de pánico? (Llamar a algún familiar, amigo, persona de confianza o especialista en salud mental)/Panic button?(call a family member, friend, trusted person or mental health specialist).")
#dtype={'caption' : str}
#plt.title("Panic Button")
#st.pyplot(fig6)

#figure 7
#fig7 = plt.figure(figsize=(4, 3))
#sns.countplot(data=df, x= df.columns[12])
#dtype={'caption' : str}
#plt.title("Share your data with family, friends or acquaintances to see your progress?")
#st.pyplot(fig7)

#figure8
#fig8 = plt.figure(figsize=(4, 3))
#sns.clustermap(data=df3)
#plt.title("App Results")
#st.pyplot(fig8)

#figure9
#fig9 = plt.figure(figsize=(4, 3))
#g = sns.JointGrid(x="Pre-Drive for Thinness", y="Result-Drive for Thinness", data=df3)
#g = g.plot(sns.regplot, sns.distplot)
#st.pyplot(fig9)

#option = st.selectbox('How would you like to be contacted?',
   #('Email', 'Home phone', 'Mobile phone'))
 #st.write('You selected:', option)



#sns.countplot(data=df, x= 'Has usado alguna app recomendada por un especialista en salud mental?/Have you used an app recommended by a mental health specialist?')
#dtype={'caption' : str}
#plt.title("Have you used an app recommended by a mental health specialist?")
#st.pyplot(fig1)


# Display Images
 
# import Image from pillow to open images
# display image using streamlit
# width is used to set the width of an image
# st.image(img, width=200)

#st.markdown(
#"""
#### The following list won't indent no matter what I try:
#- Item 1
# Item 2
#- Item 3
#"""
#)