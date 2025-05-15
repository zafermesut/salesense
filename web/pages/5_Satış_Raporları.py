import streamlit as st
import pandas as pd
import analysis as an
import plotly.express as px
import locale
from authenticate import check_session
from streamlit_extras.switch_page_button import switch_page

if not check_session():
    st.warning("Lütfen önce giriş yapınız.")
    switch_page("login")  
    st.stop()   

locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')  # For Linux/Mac 
# locale.setlocale(locale.LC_TIME, 'turkish')  # For Windows 

st.set_page_config(
    page_title="Sales Report",
    page_icon = ":bar_chart:",
    layout="wide")

st.title("Satış Raporları")

tabs = st.tabs(["Ürünler", "Müşteriler", "Coğrafi Satışlar", "Satış Trendi"])


# PRODUCT SALES TAB
with tabs[0]:
    st.subheader("📊 Ürünler")
    st.write("Bu bölümde ürün satışlarına genel bir bakış yer almaktadır.")

    most_sold, least_sold, most_exp, cheapest, most_profitable = an.get_sales_report()

    expander_p = st.expander("En Kârlı Ürünler",expanded=False)
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

    expander_ts = st.expander("En Çok Satılan Ürünler",expanded=False)
    fig = px.bar(most_sold,
                    x="name",
                    y="quantity",
                    color="quantity",
                    color_continuous_scale='Cividis')
    fig.update_layout(showlegend=False)
    expander_ts.plotly_chart(fig, use_container_width=True)
    expander_ts.write(most_sold[["name", "quantity"]].head(7))

    expander_ls = st.expander("En Az Satılan Ürünler",expanded=False)
    fig = px.bar(least_sold,
                    x="name",
                    y="quantity",
                    color="quantity",
                    color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(showlegend=False)
    expander_ls.plotly_chart(fig, use_container_width=True)
    expander_ls.write(least_sold[["name", "quantity"]].head(7))

    expander_me = st.expander("En Pahalı Ürünler",expanded=False)
    fig = px.bar(most_exp,
                    x="name",
                    y="unit_price",
                    color="unit_price",
                    color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(showlegend=False)
    expander_me.plotly_chart(fig, use_container_width=True)
    expander_me.write(most_exp[["name", "unit_price"]].head(7))

    expander_cp = st.expander("En Ucuz Ürünler",expanded=False)
    fig = px.bar(cheapest,
                    x="name",
                    y="unit_price",
                    color="unit_price",
                    color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(showlegend=False)
    expander_cp.plotly_chart(fig, use_container_width=True)
    expander_cp.write(cheapest[["name", "unit_price"]].head(7))

# CUSTOMER INSIGHTS TAB
with tabs[1]:
    st.subheader(":busts_in_silhouette: Müşteriler")
    st.write("Bu bölümde müşteri analizleri yer almaktadır.")

    rfm_contaier = st.container()
    with rfm_contaier:
        st.subheader("RFM Analizi")
        st.write("""
                    RFM (Recency, Frequency, Monetary) analizi, müşteri segmentasyonu için kullanılan güçlü bir yöntemdir. 
                    Bu analiz, müşterilerin işletme ile olan etkileşimlerini üç ana faktöre göre değerlendirir:
                    - **Recency (Yakınlık):** Müşterinin en son yaptığı alışverişin üzerinden geçen zaman.
                    - **Frequency (Sıklık):** Müşterinin belirli bir zaman diliminde yaptığı toplam alışveriş sayısı.
                    - **Monetary (Parasal Değer):** Müşterinin toplam harcama miktarı.
                """)
        rfm = an.get_rfm_analysis()
        rfm_segments = an.get_rfm_segments(rfm)


        expander_rec = st.expander("Yakınlık Dağılımı",expanded=False)
        fig = px.histogram(rfm, 
                        x="Recency", 
                        title="Yakınlık Dağılımı",
                        color_discrete_sequence=["#636EFA"])
        expander_rec.plotly_chart(fig, use_container_width=True)

        expander_freq = st.expander("Sıklık Dağılımı",expanded=False)
        fig = px.histogram(rfm, 
                        x="Frequency", 
                        title="Sıklık Dağılımı",
                        color_discrete_sequence=["#EF553B"],
                        nbins=20)
        expander_freq.plotly_chart(fig, use_container_width=True)

        expander_mon = st.expander("Parasal Dağılım",expanded=False)
        fig = px.histogram(rfm,
                        x="Monetary",
                        title="Parasal Dağılım",
                        color_discrete_sequence=["#00CC96"],
                        nbins=20)
        expander_mon.plotly_chart(fig, use_container_width=True)

        expander_rf = st.expander("Yakınlık vs Sıklık",expanded=False)
        fig = px.scatter(rfm, x="Recency",
                        y="Frequency", 
                        title="Yakınlık vs Sıklık",
                        color_discrete_sequence=["#AB63FA"])
        expander_rf.plotly_chart(fig, use_container_width=True)

        expander_rm = st.expander("Yakınlık vs Parasal Değer",expanded=False)
        fig = px.scatter(rfm, x="Recency",
                        y="Monetary", 
                        title="Yakınlık vs Parasal Değer",
                        color_discrete_sequence=["#FFA15A"])
        expander_rm.plotly_chart(fig, use_container_width=True)

        expander_fm = st.expander("Sıklık vs Parasal Değer",expanded=False)
        fig = px.scatter(rfm, x="Frequency",
                        y="Monetary", 
                        title="Sıklık vs Parasal Değer",
                        color_discrete_sequence=["#19D3F3"])
        expander_fm.plotly_chart(fig, use_container_width=True)

        expander_3d = st.expander("3D Grafik",expanded=False)
        fig = px.scatter_3d(rfm,
                            x="Recency", 
                            y="Frequency", 
                            z="Monetary", 
                            color="Monetary",
                            color_continuous_scale='Darkmint')
        expander_3d.plotly_chart(fig, use_container_width=True)



    cs_container = st.container()
    with cs_container:
        st.subheader("Müşteri Segmentasyonu")
        st.write("""
                    Müşteri segmentasyonu, müşterilerin özelliklerine göre farklı gruplara ayrılmasını sağlar. 
                    Bu segmentasyon, işletmelerin müşterilerini daha iyi anlamalarına, hedeflenmiş pazarlama stratejileri geliştirmelerine ve müşteri memnuniyetini artırmalarına yardımcı olur. 

                    **Bu Analizdeki Segmentler:**
                    - **Şampiyonlar:** En yakın zamanda alışveriş yapan, sık alışveriş yapan ve yüksek harcamalar yapan müşteriler.
                    - **Sadık Müşteriler:** Düzenli alışveriş yapan, uzun süreli sadakat gösteren müşteriler.
                    - **Potansiyel Sadıklar:** Daha fazla alışveriş yapma potansiyeli taşıyan müşteriler.
                    - **Risk Altındaki Müşteriler:** Son zamanlarda alışveriş yapmayan, kaybedilme riski taşıyan müşteriler.
                    - **Kaybedilmiş Müşteriler:** Uzun süredir alışveriş yapmayan müşteriler.

                    **Grafikler:**
                    Sol grafikte müşteri segmentlerinin dağılımını, sağ grafikte ise her segmentin toplam parasal değerini görebilirsiniz.
                """)
        
        st.dataframe(rfm_segments)

        col1, col2 = st.columns(2)  

        with col1:
            segment_counts = rfm_segments['Segment'].value_counts().reset_index()
            segment_counts.columns = ['Segment', 'Count']
            fig = px.pie(segment_counts,
                        values='Count',
                        names='Segment',
                        title='Müşteri Segmentasyonu',
                        color_discrete_sequence=px.colors.qualitative.Set3)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            monetary_per_segment = rfm_segments.groupby('Segment')['Monetary'].sum().reset_index()
            monetary_per_segment.columns = ['Segment', 'Monetary']
            fig = px.pie(monetary_per_segment,
                        values='Monetary',
                        names='Segment',
                        title='Segmentlere Göre Parasal Değer',
                        color_discrete_sequence=px.colors.qualitative.Set3)
            st.plotly_chart(fig, use_container_width=True)

        col1, col2 = st.columns(2)  
        with col1:
            fig = px.scatter(rfm_segments, x='Frequency', y='Monetary', color='Segment',
                            title='Sıklık vs. Parasal Değer',
                            color_discrete_sequence=px.colors.qualitative.Set3)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.box(rfm_segments, x='Segment', y='Recency', color='Segment',
                        title='Yakınlık Dağılımı',
                        color_discrete_sequence=px.colors.qualitative.Set3)
            st.plotly_chart(fig, use_container_width=True)
        
# GEOGRAPHICAL SALES TAB
with tabs[2]:
    st.subheader(":globe_with_meridians: Coğrafi Satışlar")
    st.write("Bu bölümde coğrafi satışların analizi yer almaktadır.")
    
    sales = an.get_geo_top_products()
    fig_choropleth = px.choropleth(sales,
                        locations='country',
                        locationmode='country names',
                        color='total_price_total',
                        hover_name='country',
                        hover_data=['name', 'total_price_top_product'],
                        title="Ülkelere Göre Satışlar",
                        color_continuous_scale='Viridis')
    st.plotly_chart(fig_choropleth, use_container_width=True)

    st.write("En çok satış yapılan ülke: **{}**".format(sales['country'].iloc[0]))
    st.dataframe(sales, width=1200)

# SALES TREND TAB
with tabs[3]:
    st.subheader(":chart_with_upwards_trend: Satış Trendi")
    st.write("Bu bölümde satış trendleri yer almaktadır.")

    expander_ms = st.expander("Aylık Satışlar",expanded=False)
    monthly_sales = an.get_monthly_sales()
    fig = px.line(monthly_sales,
                x='month_label',
                y='total_price',
                title='Aylık Satış Trendi',
                labels={'month_label': 'Ay', 'total_price': 'Toplam Satış'},
                color_discrete_sequence=['#636EFA'])
    expander_ms.plotly_chart(fig, use_container_width=True)

    expander_hs = st.expander("Saatlik Satışlar",expanded=False)
    hourly_sales = an.get_hourly_sales()
    fig = px.bar(hourly_sales,
                x='hour',
                y='total_price',
                title='Saatlik Satış Analizi',
                labels={'hour': 'Saat', 'total_price': 'Toplam Satış'},
                color_discrete_sequence=['#636EFA'])
    fig.update_xaxes(title_text='Saat (0-23)')
    fig.update_yaxes(title_text='Toplam Satış')
    expander_hs.plotly_chart(fig, use_container_width=True)

    expander_ws = st.expander("Haftalık Satışlar",expanded=False)
    weekly_sales, weekday_labels = an.get_weekly_sales() 
    fig = px.bar(weekly_sales,
                x='weekday_name', 
                y='total_price',
                title='Haftanın Günlerine Göre Toplam Satış',
                labels={'weekday_name': 'Haftanın Günü', 'total_price': 'Toplam Satış'},
                color='total_price',
                color_continuous_scale='Viridis')

    fig.update_xaxes(title_text='Haftanın Günü', categoryorder='array', categoryarray=weekday_labels)
    fig.update_yaxes(title_text='Toplam Satış')
    expander_ws.plotly_chart(fig, use_container_width=True)
