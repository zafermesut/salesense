import streamlit as st
import analysis as an
from streamlit_card import card
from plotly.tools import FigureFactory as ff

st.set_page_config(
    page_title="Anasayfa", 
    page_icon=":sunny:", 
    layout="wide")


st.title("Bilen Ticaret")

st.subheader("Genel Bakış")
products, customers, sales, countries, sales_last_week_count, customers_last_week_count = an.get_count_tables()
# 4 cols
col1, col2, col3, col4 = st.columns(4)
with col1:
    con1 = st.container(border=True)
    con1.metric(label="Toplam Satış", value=sales, delta="{} (1 Hafta)".format(sales_last_week_count))
with col2:
    con2 = st.container(border=True)
    con2.metric(label="Toplam Ürün", value=products, delta=0)
with col3:
    con3 = st.container(border=True)
    con3.metric(label="Toplam Müşteri", value=customers, delta=customers_last_week_count)
with col4:
    con4 = st.container(border=True)
    con4.metric(label="Toplam Ülke", value=countries, delta=0)


st.subheader("Son Satışlar")
last_sales = an.get_last_sales()
st.dataframe(last_sales)



