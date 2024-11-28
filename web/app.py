import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

# Sayfa yapılandırması
st.set_page_config(page_title="Sales Report Tabs", layout="wide")

df = pd.read_csv("../data/cleaned_data.csv")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",  # Menü başlığı
        options=["Dashboard", "Users", "Sales", "Sales Report", "Recommendations"],  # Menü seçenekleri
        icons=["grid", "person", "currency-dollar", "bar-chart", "lightbulb"],  # Menü simgeleri
        menu_icon="menu-button",  # Menü ikonu
        default_index=3,  # Varsayılan seçim
    )

# Boş bırakılan menüler
if selected == "Dashboard":
    st.title("Dashboard")
    st.write("Dashboard content goes here...")

elif selected == "Users":
    st.title("Users")
    st.write("User management content goes here...")

elif selected == "Sales":
    st.title("Sales")
    st.write("Sales data content goes here...")

elif selected == "Recommendations":
    st.title("Recommendations")
    st.write("AI-based recommendations content goes here...")

# Sales Report with Tabs
elif selected == "Sales Report":
    st.title("Sales Report")

    # Tabs for Sales Report
    tabs = st.tabs(["📊 Product Sales", "📑 Charts", "📉 Trends"])

    with tabs[0]:
        st.subheader("📊 Product Sales")
        st.write("This section contains an overview of product sales.")

        container_ts = st.container(border=True)
        container_ts.write("### Most Sold Products")
        most_sold = df.groupby("Description")["Quantity"].sum().reset_index()
        most_sold = most_sold.sort_values("Quantity", ascending=False).head(5)
        fig = px.bar(most_sold, x="Description", y="Quantity", title="Chart: Most Sold")
        container_ts.plotly_chart(fig, use_container_width=True)


        container_me = st.container(border=True)
        container_me.write("### Most Expensive Products")
        most_exp = df.groupby("Description")["UnitPrice"].max().reset_index()
        most_exp = most_exp.sort_values("UnitPrice", ascending=False).head(5)
        fig = px.bar(most_exp, x="Description", y="UnitPrice", title="Chart: Most Expensive")
        container_me.plotly_chart(fig, use_container_width=True)
        



    with tabs[1]:
        st.subheader("📑 Charts")
        st.write("This section contains detailed charts.")
        
        # Example Pie Chart
        chart_df = pd.DataFrame({
            "Region": ["North", "South", "East", "West"],
            "Sales": [300, 400, 350, 250]
        })
        fig = px.pie(chart_df, names="Region", values="Sales", title="Sales by Region")
        st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:
        st.subheader("📉 Trends")
        st.write("This section shows trends in sales data.")
        
        # Example Line Chart
        trend_df = pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr"],
            "Sales": [100, 150, 200, 250]
        })
        fig = px.line(trend_df, x="Month", y="Sales", title="Sales Trends Over Time")
        st.plotly_chart(fig, use_container_width=True)

