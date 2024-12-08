import streamlit as st
import pandas as pd
import analysis as an
import plotly.express as px


st.set_page_config(
    page_title="Sales Report",
    page_icon = ":bar_chart:", 
    layout="wide")

st.title("Sales Report")

tabs = st.tabs(["Product Sales", "Customer Insights", "Geographical Sales", "Sales Trends"])

with tabs[0]:
    st.subheader("📊 Product Sales")
    st.write("This section contains an overview of product sales.")

    most_sold, least_sold, most_exp, cheapest, most_profitable = an.get_sales_report()

    expander_p = st.expander("Most Profitable Products",expanded=False)
    fig = px.bar(most_profitable,
                    x="name",
                    y="Profit",
                    color="Profit",
                    labels={"Profit": "Total Profit", "name": "Product"},
                    hover_data=["quantity", "unit_price"],
                    color_continuous_scale="Viridis")
    fig.update_layout(showlegend=False)
    expander_p.plotly_chart(fig, use_container_width=True)
    expander_p.write(most_profitable[["name", "Profit"]].head(7))

    expander_ts = st.expander("Most Sold Products",expanded=False)
    fig = px.bar(most_sold,
                    x="name",
                    y="quantity",
                    color="quantity",
                    color_continuous_scale='Cividis')
    fig.update_layout(showlegend=False)
    expander_ts.plotly_chart(fig, use_container_width=True)
    expander_ts.write(most_sold[["name", "quantity"]].head(7))

    expander_ls = st.expander("Least Sold Products",expanded=False)
    fig = px.bar(least_sold,
                    x="name",
                    y="quantity",
                    color="quantity",
                    color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(showlegend=False)
    expander_ls.plotly_chart(fig, use_container_width=True)
    expander_ls.write(least_sold[["name", "quantity"]].head(7))

    expander_me = st.expander("Most Expensive Products",expanded=False)
    fig = px.bar(most_exp,
                    x="name",
                    y="unit_price",
                    color="unit_price",
                    color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(showlegend=False)
    expander_me.plotly_chart(fig, use_container_width=True)
    expander_me.write(most_exp[["name", "unit_price"]].head(7))

    expander_cp = st.expander("Cheapest Products",expanded=False)
    fig = px.bar(cheapest,
                    x="name",
                    y="unit_price",
                    color="unit_price",
                    color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(showlegend=False)
    expander_cp.plotly_chart(fig, use_container_width=True)
    expander_cp.write(cheapest[["name", "unit_price"]].head(7))

with tabs[1]:
    st.subheader(":busts_in_silhouette: Customer Insights")
    st.write("This section contains insights about customers.")

    st.subheader("RFM Analysis")
    rfm = an.get_rfm_analysis()

    # Plotting a histogram of recency
    expander_rec = st.expander("Recency Distribution",expanded=False)
    fig = px.histogram(rfm, 
                       x="Recency", 
                       title="Recency Distribution",
                       color_discrete_sequence=["#636EFA"])
    expander_rec.plotly_chart(fig, use_container_width=True)

    # Plotting a histogram of frequency
    expander_freq = st.expander("Frequency Distribution",expanded=False)
    fig = px.histogram(rfm, 
                       x="Frequency", 
                       title="Frequency Distribution",
                       color_discrete_sequence=["#EF553B"],
                       nbins=20)
    expander_freq.plotly_chart(fig, use_container_width=True)

    # Plotting a histogram of monetary
    expander_mon = st.expander("Monetary Distribution",expanded=False)
    fig = px.histogram(rfm,
                       x="Monetary",
                       title="Monetary Distribution",
                       color_discrete_sequence=["#00CC96"],
                       nbins=20)
    expander_mon.plotly_chart(fig, use_container_width=True)

    #Scatter plot of Recency vs Frequency
    expander_rf = st.expander("Recency vs Frequency",expanded=False)
    fig = px.scatter(rfm, x="Recency",
                     y="Frequency", 
                     title="Recency vs Frequency",
                     color_discrete_sequence=["#AB63FA"])
    expander_rf.plotly_chart(fig, use_container_width=True)

    #Scatter plot of Recency vs Monetary
    expander_rm = st.expander("Recency vs Monetary",expanded=False)
    fig = px.scatter(rfm, x="Recency",
                     y="Monetary", 
                     title="Recency vs Monetary",
                     color_discrete_sequence=["#FFA15A"])
    expander_rm.plotly_chart(fig, use_container_width=True)

    #Scatter plot of Frequency vs Monetary
    expander_fm = st.expander("Frequency vs Monetary",expanded=False)
    fig = px.scatter(rfm, x="Frequency",
                     y="Monetary", 
                     title="Frequency vs Monetary",
                     color_discrete_sequence=["#19D3F3"])
    expander_fm.plotly_chart(fig, use_container_width=True)

    #Plotting 3D scatter plot
    expander_3d = st.expander("3D Scatter Plot",expanded=False)
    fig = px.scatter_3d(rfm,
                        x="Recency", 
                        y="Frequency", 
                        z="Monetary", 
                        color="Monetary",
                        color_continuous_scale='Darkmint')
    expander_3d.plotly_chart(fig, use_container_width=True)



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