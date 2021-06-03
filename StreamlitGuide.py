import streamlit as st 
from PIL import Image
import numpy as np
import pandas as pd

st.write("Ciao!")

st.write("Ciao di nuvo!")

st.write("Ciao di nuovo! DI nuovo ?")

st.write("""

### Titolo markdown. 

##### Sottotitolo markdown

- punto primo 
- punto secondo 
- punto terzo

""")

st.header("Intestazione!")
st.subheader("Sottotitolo!")

st.text("Ecco un po di testo di prova!")

st.markdown("### Riga Markdown")

st.success("Codice eseguito!")
st.info("Punto ionforamzioni: clica per informarti ")
st.warning("Attenzione! Hai dimenticato di avviare l'ambiente viortuale!")

st.error("Errore! ")

st.help(sorted)

image = Image.open("bordercollie.jpg")

st.image(image, width= 300)

df = pd.DataFrame({"paolo":[200, 300, 400], "ste":[300, 400, 500], "fra":[400, 500, 800]})

st.dataframe(df)  

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    
    
genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy': st.write('You selected comedy.')
else: st.write("You didn't select comedy.") 


option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

numero = st.number_input("Enter number ..")
st.write(numero)

st.sidebar.header("Menu")
st.sidebar.text("Analizza i dati con alg1")
st.sidebar.text("Analizza i dati con alg2")
st.sidebar.text("Analizza i dati con alg3")
st.sidebar.image(image)
