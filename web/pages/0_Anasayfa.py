import streamlit as st
import analysis as an
from authenticate import check_session
from streamlit_extras.switch_page_button import switch_page

if not check_session():
    st.warning("Lütfen önce giriş yapınız.")
    switch_page("login")  
    st.stop()    
            
st.set_page_config(
    page_title="Anasayfa",
    page_icon="🏠",
    layout="wide"
)

username = st.session_state.get("username")

text = f"Hoş Geldin {username} 👋" if username else "Hoş Geldin 👋"
# Ana sayfa içeriği
st.title(text)



# İstatistikler
products, customers, sales, countries, sales_last_week, customers_last_week = an.get_count_tables()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info(f"**Toplam Ürün**  \n{products:,}", icon="📦")

with col2:
    st.info(f"**Toplam Müşteri**  \n{customers:,}", icon="👥")
    
with col3:
    st.info(f"**Toplam Satış**  \n{sales:,}", icon="💰")
    
with col4:
    st.info(f"**Toplam Ülke**  \n{countries:,}", icon="🌍")

st.divider()

# Son hafta istatistikleri
st.subheader("Son 7 Gün")
col1, col2 = st.columns(2)

with col1:
    st.success(f"**Satış Sayısı**  \n{sales_last_week:,}", icon="📈")
    
with col2:
    st.success(f"**Aktif Müşteri**  \n{customers_last_week:,}", icon="👥")

st.divider()

# Son satışlar
st.subheader("Son Satışlar")
last_sales = an.get_last_sales()
st.dataframe(last_sales, use_container_width=True)



