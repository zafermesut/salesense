import streamlit as st
import pandas as pd
import analysis as an

st.set_page_config(
    page_title="Satışlar", 
    page_icon = ":heavy_dollar_sign:", 
    layout="wide")

st.title("Satışlar")

sales = an.get_sales_data()

st.write("Toplam {:,} satış yapılmıştır.".format(len(sales)))
st.dataframe(sales, height=600, width=1400)

