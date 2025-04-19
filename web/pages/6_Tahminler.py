import streamlit as st
import pandas as pd
import analysis as an
from prophet import Prophet
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Tahminler", 
    page_icon = "🎯", 
    layout="wide")

st.title("🎯 Tahminler")

# Ürün listesi
monthly_sales = an.get_monthly_sales_by_product()

product_list = monthly_sales['name'].unique()
selected_product = st.selectbox("Ürün Seçin", product_list)

if st.button("Tahmin Et"):
    product_data = monthly_sales[monthly_sales['name'] == selected_product]
    df_prophet = product_data.rename(columns={'year_month': 'ds', 'quantity': 'y'})
    df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])

    model = Prophet()
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=1, freq='M')
    forecast = model.predict(future)
    
    predicted = forecast[['ds', 'yhat']].tail(1).values[0]
    st.success(f"📦 {selected_product} ürününün tahmini satış miktarı: {int(predicted[1])} adet ({predicted[0].strftime('%B %Y')})")
