import streamlit as st
import analysis as an
from authenticate import check_session
from streamlit_extras.switch_page_button import switch_page

if not check_session():
    st.warning("Lütfen önce giriş yapınız.")
    switch_page("login")  
    st.stop()

st.set_page_config(page_title="Ayarlar", page_icon=":gear:", layout="wide")

st.title("Ayarlar")

current_email = st.session_state.get("email")  

user = an.get_user_by_email(current_email)
if user:
    user_id, user_email, user_name = user
else:
    st.error("Kullanıcı bulunamadı!")
    st.stop()

st.subheader("Mevcut Kullanıcı Bilgileri")

with st.form("update_user_form"):
    new_email = st.text_input("Email", value=user_email)
    new_username = st.text_input("Kullanıcı Adı", value=user_name)
    new_password = st.text_input("Yeni Şifre (boş bırakılırsa değişmez)", type="password")

    update_btn = st.form_submit_button("Bilgileri Güncelle")

if update_btn:
    if new_email and new_username:
        an.update_user(user_id, new_email, new_username, new_password if new_password else None)
        st.success("Bilgiler başarıyla güncellendi.")
        st.session_state["email"] = new_email  # session'u güncelle
    else:
        st.error("Email ve kullanıcı adı boş olamaz.")

st.markdown("---")

st.subheader("Yeni Kullanıcı Ekle")

with st.form("add_user_form"):
    new_user_email = st.text_input("Email", key="new_user_email")
    new_user_username = st.text_input("Kullanıcı Adı", key="new_user_username")
    new_user_password = st.text_input("Şifre", type="password", key="new_user_password")

    add_user_btn = st.form_submit_button("Kullanıcı Ekle")

if add_user_btn:
    if new_user_email and new_user_username and new_user_password:
        try:
            an.add_user(new_user_email, new_user_username, new_user_password)
            st.success(f"{new_user_username} başarıyla eklendi.")
            # Formu temizle
            st.session_state.pop("new_user_email", None)
            st.session_state.pop("new_user_username", None)
            st.session_state.pop("new_user_password", None)
        except Exception as e:
            st.error(f"Kullanıcı eklenirken hata oluştu: {e}")
    else:
        st.error("Tüm alanları doldurun.")

st.markdown("---")

st.subheader("Mevcut Kullanıcılar")

users = an.get_all_users()
if not users.empty:
    st.dataframe(users)
else:
    st.info("Henüz kullanıcı bulunmamaktadır.")

st.markdown("---")

st.subheader("Şirket Ayarları")
name = st.text_input("Şirket Adı", value=an.get_settings_data()[0])
desc = st.text_area("Açıklama", value=an.get_settings_data()[1], height=200)

if st.button("Kaydet"):
    an.save_settings_data(name, desc)
    st.success("Ayarlar başarıyla kaydedildi.")
