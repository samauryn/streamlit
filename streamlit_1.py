import streamlit as st
import pandas as pd
import pydeck as pdk

df = pd.read_excel("Earphone Adiletkhan.xlsx", sheet_name="Лист4")

st.dataframe(df)
