import numpy as np
import pandas as pd
import database as db 

def get_sales_data():
    sales = db.query_db("SELECT * FROM sales")
    return sales

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

    # Frequency
    frequency = sales.groupby('customer_id')['invoice_date'].nunique()

    # Monetary
    monetary = sales.groupby('customer_id')['total_price'].sum()

    rfm_df = pd.DataFrame({
    'Recency': recency,
    'Frequency': frequency,
    'Monetary': monetary
    })

    return rfm_df

  

