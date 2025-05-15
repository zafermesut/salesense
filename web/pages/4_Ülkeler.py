import streamlit as st
import pandas as pd
import analysis as an
from authenticate import check_session
from streamlit_extras.switch_page_button import switch_page

if not check_session():
    st.warning("Lütfen önce giriş yapınız.")
    switch_page("login")  
    st.stop()   

st.set_page_config(
    page_title="Ülkeler", 
    page_icon = ":earth_americas:", 
    layout="wide")

st.title("🌎 Ülkeler")

countries = an.get_countries_data()

st.write("Toplam {} ülkeye satış yapılmıştır.".format(len(countries))) 
st.dataframe(countries, height=600, width=1000)

