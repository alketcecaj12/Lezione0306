import streamlit as st
import pickle
import numpy as np 

st.write("Interfaccia previsone test di diabete! ")

st.write("Interfaccia costruita con Streamlit!")

# caricao il modello 
with open("modelli/modello_class.pkl", "rb") as model_file: 
     model = pickle.load(model_file)
     
     

p = st.number_input("Inserisci pregnacies: ")
g = st.number_input("Inserisci livello glucosio: ")
ps = st.number_input("Inserisci pressione sanguinea: ")

xi = np.array([p, g, ps]).reshape(1 , -1)


previsione = model.predict(xi)


st.write("Ecco la previsione per il test.")
st.write(previsione[0])