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
    page_title="Ürünler", 
    page_icon = ":shopping_trolley:", 
    layout="wide")

st.title("🛍️ Ürünler")

products = an.get_products_data()

st.write("Toplam {:,} ürün bulunmaktadır.".format(len(products))) 
st.dataframe(products, height=600, width=1400)

