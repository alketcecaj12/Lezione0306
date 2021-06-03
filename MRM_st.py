import streamlit as st
import pickle
import numpy as np 

st.write("Interfaccia previsone vendite data la distribuzione budget pubblicitario. ")

st.write("Interfaccia costruita con Streamlit!")

# caricao il modello 
with open("modelli/modello_migliore.pkl", "rb") as model_file: 
     model = pickle.load(model_file)
     
     

in_tv = st.number_input("Inserisci spese TV")
in_r  = st.number_input("Inserisci spese Radio")
in_g  = st.number_input("Inserisci spese Giornale")     


values = np.array([in_tv, in_r, in_g]).reshape(1, -1)
    
previsione = int(model.predict(values))

st.write("Ecco le previsioni di vendita data una particolare distribuzione del budget!")
st.write(previsione)