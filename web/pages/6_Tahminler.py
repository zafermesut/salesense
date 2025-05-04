import streamlit as st
import pandas as pd
import analysis as an
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objects as go
import warnings

warnings.filterwarnings("ignore")

# Sayfa ayarları
st.set_page_config(
    page_title="Tahminler", 
    page_icon="🎯", 
    layout="wide"
)

st.title("🎯 Satış Tahmin Paneli")

# Ürün verisi
monthly_sales = an.get_monthly_sales_by_product()
product_list = monthly_sales['name'].unique()

# Arayüz
selected_product = st.selectbox("🛒 Ürün Seçin", product_list)
selected_model = st.selectbox("📊 Model Seçin", ["Prophet", "ARIMA"])
n_months = st.slider("📅 Tahmin Edilecek Ay Sayısı", 1, 12, 3)

if st.button("🔮 Tahmin Et"):
    product_data = monthly_sales[monthly_sales['name'] == selected_product]
    df = product_data.rename(columns={'year_month': 'ds', 'quantity': 'y'})
    df['ds'] = pd.to_datetime(df['ds'])
    df = df.sort_values("ds")

    st.subheader(f"📈 {selected_product} Ürünü - Tahmin Sonuçları")

    if selected_model == "Prophet":
        # Prophet Modeli
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=n_months, freq='M')
        forecast = model.predict(future)

        last_pred = forecast[['ds', 'yhat']].tail(n_months)
        for i, row in last_pred.iterrows():
            st.success(f"📦 {row['ds'].strftime('%B %Y')}: Tahmini Satış = {int(row['yhat'])} adet")

        # Grafik
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='lines+markers', name='Gerçek Satışlar', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines+markers', name='Tahmin', line=dict(color='orange', dash='dash')))
    
    elif selected_model == "ARIMA":
        df_arima = df.set_index('ds')['y'].asfreq('M').fillna(method='ffill')
        model = ARIMA(df_arima, order=(1, 1, 1))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=n_months)

        forecast_dates = pd.date_range(start=df_arima.index[-1] + pd.offsets.MonthBegin(), periods=n_months, freq='MS')
        last_pred = pd.DataFrame({'ds': forecast_dates, 'yhat': forecast.values})

        for i, row in last_pred.iterrows():
            st.success(f"📦 {row['ds'].strftime('%B %Y')}: Tahmini Satış = {int(row['yhat'])} adet")

        # Grafik
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_arima.index, y=df_arima.values, mode='lines+markers', name='Gerçek Satışlar', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=forecast_dates, y=forecast.values, mode='lines+markers', name='Tahmin', line=dict(color='green', dash='dash')))

    fig.update_layout(
        title=f"{selected_product} - Satış Tahmin Grafiği ({selected_model})",
        xaxis_title="Tarih",
        yaxis_title="Satış Miktarı",
        legend=dict(x=0, y=1),
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)