import streamlit as st
import pickle

import numpy as np 

st.write("Interfaccia previsone vendite ombrelli!")

st.write("interfaccia costruita con Streamli!")

st.write("test")

# caricao il modello 
with open("modelli/modello_rl.pkl", "rb") as model_file: 
     model = pickle.load(model_file)
     
     

n = st.number_input("Inserisci i mm di pioggia per ottenere la previsione : ")

x = np.array([n])

previsione = model.predict([x])

st.write("Ecco la previsione di vendita: ")
st.write(int(previsione))