import streamlit as st
import pandas as pd
import analysis as an

st.set_page_config(
    page_title="Ülkeler", 
    page_icon = ":earth_americas:", 
    layout="wide")

st.title("Ülkeler")

countries = an.get_countries_data()

st.write("Toplam {} ülkeye satış yapılmıştır.".format(len(countries))) 
st.dataframe(countries, height=600, width=1000)

