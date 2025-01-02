import streamlit as st
import pandas as pd
import analysis as an

st.set_page_config(
    page_title="Ürünler", 
    page_icon = ":shopping_trolley:", 
    layout="wide")

st.title("🛍️ Ürünler")

products = an.get_products_data()

st.write("Toplam {:,} ürün bulunmaktadır.".format(len(products))) 
st.dataframe(products, height=600, width=1400)

