import numpy as np
import pandas as pd
import database as db 

from datetime import datetime, timedelta

def get_settings_data():
    settings = db.query_db("SELECT * FROM settings")
    company_name = settings['company_name'].iloc[0]
    description = settings['description'].iloc[0]
    return company_name, description

def get_sales_data():
    sales = db.query_db("SELECT * FROM sales")
    sales['invoice_date'] = pd.to_datetime(sales['invoice_date'])
    # sort by date
    sales = sales.sort_values('invoice_date', ascending=False)
    return sales

def get_last_sales():
    last_sales = db.query_db("SELECT * FROM sales ORDER BY invoice_date DESC LIMIT 5")
    last_sales = last_sales.drop(columns=['stock_code','customer_id', 'customer_email'])
    return last_sales

def get_count_tables():
    products = db.query_db("SELECT COUNT(*) FROM products")
    customers = db.query_db("SELECT COUNT(*) FROM customers")
    sales = db.query_db("SELECT COUNT(*) FROM sales")
    countries = db.query_db("SELECT COUNT(*) FROM countries")

    # Check if results are not empty and get the count safely
    products_count = products.iloc[0, 0] if not products.empty else 0
    customers_count = customers.iloc[0, 0] if not customers.empty else 0
    sales_count = sales.iloc[0, 0] if not sales.empty else 0
    countries_count = countries.iloc[0, 0] if not countries.empty else 0

    # Get the count of sales in the last week
    sales = db.query_db("SELECT * FROM sales")
    sales['invoice_date'] = pd.to_datetime(sales['invoice_date'])
    last_week = sales['invoice_date'].max() - timedelta(days=7)
    sales_last_week = sales[sales['invoice_date'] >= last_week]
    sales_last_week_count = sales_last_week.shape[0]
    customers_last_week = sales_last_week.drop_duplicates('customer_id')
    customers_last_week_count = customers_last_week.shape[0]




    return products_count, customers_count, sales_count, countries_count, sales_last_week_count, customers_last_week_count


def get_products_data():
    products = db.query_db("SELECT * FROM products")
    return products

def get_countries_data():
    countries = db.query_db("SELECT * FROM countries")
    return countries

def get_customers_data():
    customers = db.query_db("SELECT * FROM customers")
    return customers

def get_most_sold_products(sales):
    most_sold = sales.groupby("name")["quantity"].sum().reset_index()
    most_sold = most_sold.sort_values("quantity", ascending=False).head(7)
    return most_sold

def get_least_sold_products(sales):
    least_sold = sales.groupby("name")["quantity"].sum().reset_index()
    least_sold = least_sold.sort_values("quantity", ascending=True).head(7)
    return least_sold

def get_most_expensive_products(sales):
    most_exp = sales.groupby("name")["unit_price"].max().reset_index()
    most_exp = most_exp.sort_values("unit_price", ascending=False).head(7)
    return most_exp

def get_cheapest_products(sales):
    cheapest = sales.groupby("name")["unit_price"].min().reset_index()
    cheapest = cheapest.sort_values("unit_price", ascending=True).head(7)
    return cheapest

def get_most_profitable_products(sales):
    profit_data = sales.copy()
    sales2 = sales.copy()
    profit_data["Profit"] = profit_data["quantity"] * profit_data["unit_price"] 
    most_profitable = profit_data.groupby("name")["Profit"].sum().reset_index()
    sales2["Profit"] = profit_data["Profit"]
    most_profitable = sales2
    most_profitable = most_profitable.sort_values("Profit", ascending=False).head(7)
    most_profitable['Profit'] = most_profitable['Profit'].round(2)
    return most_profitable

def get_sales_report():
    sales = get_sales_data()
    most_sold = get_most_sold_products(sales)
    least_sold = get_least_sold_products(sales)
    most_exp = get_most_expensive_products(sales)
    cheapest = get_cheapest_products(sales)
    most_profitable = get_most_profitable_products(sales)
    return most_sold, least_sold, most_exp, cheapest, most_profitable

def get_rfm_analysis():
    sales = get_sales_data()
    sales['invoice_date'] = pd.to_datetime(sales['invoice_date'])
    current_date = sales['invoice_date'].max()
    current_date

    recency = sales.groupby('customer_id')['invoice_date'].max()
    recency = (current_date - recency).dt.days

    # frequency
    frequency = sales.groupby('customer_id')['invoice_date'].nunique()

    # monetary
    monetary = sales.groupby('customer_id')['total_price'].sum()

    rfm_df = pd.DataFrame({
    'Recency': recency,
    'Frequency': frequency,
    'Monetary': monetary
    })

    return rfm_df


def segment_customer_based_on_rfm_score(row):
    if row['RFMScore'] >= 500:
        return 'Şampiyonlar'
    elif 400 <= row['RFMScore'] < 500:
        return 'Sadık Müşteriler'
    elif 300 <= row['RFMScore'] < 400:
        return 'Potansiyel Sadıklar'
    elif 200 <= row['RFMScore'] < 300:
        return 'Risk Altındaki Müşteriler'
    else:
        return 'Kaybedilmiş Müşteriler'

def get_rfm_segments(rfm_df):
    rfm_df['RecencyScore'] = pd.qcut(rfm_df['Recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm_df['FrequencyScore'] = pd.qcut(rfm_df['Frequency'], 5, labels=[1, 2, 3, 4],duplicates='drop')  
    rfm_df['MonetaryScore'] = pd.qcut(rfm_df['Monetary'], 5, labels=[1, 2, 3, 4, 5])  

    rfm_df['RFMScore'] = rfm_df['RecencyScore'].astype(str) + rfm_df['FrequencyScore'].astype(str) + rfm_df['MonetaryScore'].astype(str)
    rfm_df['RFMScore'] = pd.to_numeric(rfm_df['RFMScore'])

    rfm_df['Segment'] = rfm_df.apply(segment_customer_based_on_rfm_score, axis=1)
    rfm_df = rfm_df.sort_values('RFMScore', ascending = False)

    customers = get_customers_data()
    customers = customers.rename(columns={'CustomerID': 'customer_id'})
    rfm_df = rfm_df.merge(customers, on='customer_id')
    rfm_df = rfm_df[['customer_id', 'Recency', 'Frequency', 'Monetary', 'RFMScore', 'Segment', 'CustomerName', 'CustomerEmail']]

    return rfm_df


def get_geo_data():
    sales = get_sales_data()
    sales = sales.groupby('country')['total_price'].sum().reset_index()
    sales = sales.sort_values('total_price', ascending=False)

    return sales


def get_geo_top_products():
    sales = get_sales_data()
    product_sales = sales.groupby(['country', 'name'])['total_price'].sum().reset_index()
    top_products = product_sales.loc[product_sales.groupby('country')['total_price'].idxmax()]
    total_sales = sales.groupby('country')['total_price'].sum().reset_index()
    geo_data = total_sales.merge(top_products, on='country', suffixes=('_total', '_top_product'))
    geo_data = geo_data.sort_values('total_price_total', ascending=False)

    return geo_data

def get_monthly_sales():
    sales = get_sales_data()
    sales['invoice_date'] = pd.to_datetime(sales['invoice_date'])
    sales['month'] = sales['invoice_date'].dt.to_period('M')
    monthly_sales = sales.groupby('month')['total_price'].sum().reset_index()
    monthly_sales['month_label'] = monthly_sales['month'].dt.strftime('%B %Y') 
    monthly_sales = monthly_sales.sort_values('month')

    return monthly_sales

def get_hourly_sales():
    sales = get_sales_data()
    sales['invoice_date'] = pd.to_datetime(sales['invoice_date'])
    sales['hour'] = sales['invoice_date'].dt.hour  
    hourly_sales = sales.groupby('hour')['total_price'].sum().reset_index()

    return hourly_sales

def get_weekly_sales():
    sales = get_sales_data()
    sales['invoice_date'] = pd.to_datetime(sales['invoice_date'])
    sales['weekday'] = sales['invoice_date'].dt.weekday
    weekly_sales = sales.groupby('weekday')['total_price'].sum().reset_index()
    weekday_labels = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
    weekly_sales['weekday_name'] = weekly_sales['weekday'].apply(lambda x: weekday_labels[x])

    return weekly_sales, weekday_labels

def save_settings_data(name, desc):
    db.update_db("UPDATE settings SET company_name = '{}', description = '{}'".format(name, desc))
    return

