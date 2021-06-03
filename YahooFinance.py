import pandas as pd
import yfinance as yf
import streamlit as st

st.header("Applicazione che si connette a YF e visualizza i dati!")
t = yf.Ticker("AAPL")
dati = t.history(period = "5Y")

st.write(dati.head())

#dati["Close"]

st.line_chart(dati["Close"])

dati["Return"]= dati["Close"].pct_change()* 100

st.line_chart(dati["Return"])