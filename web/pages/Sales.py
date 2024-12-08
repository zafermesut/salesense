import streamlit as st
import pandas as pd
import analysis as an

st.set_page_config(
    page_title="Sales", 
    page_icon = ":heavy_dollar_sign:", 
    layout="wide")

st.title("Sales")

sales = an.get_sales_data()

st.dataframe(sales, height=600)

