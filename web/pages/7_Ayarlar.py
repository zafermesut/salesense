import streamlit as st
import analysis as an


st.set_page_config(
    page_title="Ayarlar", 
    page_icon = ":gear:", 
    layout="wide")


st.title("Ayarlar")

st.subheader("Kullanıcı Ayarları")
st.write("KULLANICI AYARLARI.")
# TODO KULLANICI EKLENECEK



st.subheader("Şirket Ayarları")
name = st.text_input("Şirket Adı", value=an.get_settings_data()[0])
desc = st.text_area("Açıklama", value=an.get_settings_data()[1], height=200)

save = st.button("Kaydet", on_click=an.save_settings_data(name, desc))
if save:
    st.success("Ayarlar başarıyla kaydedildi.")


