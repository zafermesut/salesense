import streamlit as st
from authenticate import login, check_session
from streamlit_extras.switch_page_button import switch_page

def login_page():
    st.title("Giriş Yap")

    # Eğer kullanıcı zaten login ise anasayfaya yönlendir
    if check_session():
        switch_page("anasayfa")


    # Login formu
    email = st.text_input("Email")
    password = st.text_input("Şifre", type="password")

    if st.button("Giriş Yap"):
        if login(email, password):
            switch_page("anasayfa")
        else:
            st.error("Email veya şifre hatalı!")

if __name__ == "__main__":
    login_page()