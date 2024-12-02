import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Report Tabs", layout="wide")

df = pd.read_csv("../data/cleaned_data.csv")

with st.sidebar:
    selected = option_menu(
        menu_title="Navigation", 
        options=["Dashboard", "Users", "Sales", "Sales Report", "Recommendations"],  
        icons=["grid", "person", "currency-dollar", "bar-chart", "lightbulb"], 
        menu_icon="menu-button",  
        default_index=3,  
    )

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

elif selected == "Sales Report":
    st.title("Sales Report")

    tabs = st.tabs(["Product Sales", "Customer Insights", "Geographical Sales", "Sales Trends"])

    with tabs[0]:
        st.subheader("📊 Product Sales")
        st.write("This section contains an overview of product sales.")

        most_sold = df.groupby("Description")["Quantity"].sum().reset_index()
        most_sold = most_sold.sort_values("Quantity", ascending=False).head(7)

        least_sold = df.groupby("Description")["Quantity"].sum().reset_index()
        least_sold = least_sold.sort_values("Quantity", ascending=True).head(7)

        most_exp = df.groupby("Description")["UnitPrice"].max().reset_index()
        most_exp = most_exp.sort_values("UnitPrice", ascending=False).head(7)

        cheapest = df.groupby("Description")["UnitPrice"].min().reset_index()
        cheapest = cheapest.sort_values("UnitPrice", ascending=True).head(7)

        profit_data = df.copy()
        df2 = df.copy()
        profit_data["Profit"] = profit_data["Quantity"] * profit_data["UnitPrice"] 
        most_profitable = profit_data.groupby("Description")["Profit"].sum().reset_index()
        df2["Profit"] = profit_data["Profit"]
        most_profitable = df2
        most_profitable = most_profitable.sort_values("Profit", ascending=False).head(7)
        most_profitable['Profit'] = most_profitable['Profit'].round(2)

        expander_p = st.expander("Most Profitable Products",expanded=False)
        fig = px.bar(most_profitable,
                     x="Description",
                     y="Profit",
                     color="Profit",
                     labels={"Profit": "Total Profit", "Description": "Product"},
                     hover_data=["Quantity", "UnitPrice"],
                     color_continuous_scale="Viridis")
        fig.update_layout(showlegend=False)
        expander_p.plotly_chart(fig, use_container_width=True)
        expander_p.write(most_profitable[["Description", "Profit"]].head(7))

        expander_ts = st.expander("Most Sold Products",expanded=False)
        fig = px.bar(most_sold,
                     x="Description",
                     y="Quantity",
                     color="Quantity",
                     color_continuous_scale='Cividis')
        fig.update_layout(showlegend=False)
        expander_ts.plotly_chart(fig, use_container_width=True)
        expander_ts.write(most_sold[["Description", "Quantity"]].head(7))

        expander_ls = st.expander("Least Sold Products",expanded=False)
        fig = px.bar(least_sold,
                     x="Description",
                     y="Quantity",
                     color="Quantity",
                     color_continuous_scale=px.colors.sequential.Viridis)
        fig.update_layout(showlegend=False)
        expander_ls.plotly_chart(fig, use_container_width=True)
        expander_ls.write(least_sold[["Description", "Quantity"]].head(7))

        expander_me = st.expander("Most Expensive Products",expanded=False)
        fig = px.bar(most_exp,
                     x="Description",
                     y="UnitPrice",
                     color="UnitPrice",
                     color_continuous_scale=px.colors.sequential.Viridis)
        fig.update_layout(showlegend=False)
        expander_me.plotly_chart(fig, use_container_width=True)
        expander_me.write(most_exp[["Description", "UnitPrice"]].head(7))

        expander_cp = st.expander("Cheapest Products",expanded=False)
        fig = px.bar(cheapest,
                     x="Description",
                     y="UnitPrice",
                     color="UnitPrice",
                     color_continuous_scale=px.colors.sequential.Viridis)
        fig.update_layout(showlegend=False)
        expander_cp.plotly_chart(fig, use_container_width=True)
        expander_cp.write(cheapest[["Description", "UnitPrice"]].head(7))

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

