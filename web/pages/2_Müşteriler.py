import streamlit as st
import pandas as pd
import analysis as an

st.set_page_config(
    page_title="Müşteriler", 
    page_icon = ":busts_in_silhouette:", 
    layout="wide")

st.title("Müşteriler")

customers = an.get_customers_data()

st.write("Toplam {} müşteri alışveriş yapmıştır.".format(len(customers))) 
st.dataframe(customers, height=600, width=1400)