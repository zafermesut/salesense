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
    page_title="Müşteriler", 
    page_icon = ":busts_in_silhouette:", 
    layout="wide")

st.title("👥 Müşteriler")

customers = an.get_customers_data()

st.write("Toplam {} müşteri alışveriş yapmıştır.".format(len(customers))) 
st.dataframe(customers, height=600, width=1400)