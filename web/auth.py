import streamlit as st
import extra_streamlit_components as stx
import datetime
import uuid

def get_cookie_manager():
    if 'cookie_manager' not in st.session_state:
        st.session_state.cookie_manager = stx.CookieManager(key=f"cookies_{uuid.uuid4().hex}")
    return st.session_state.cookie_manager

def check_authentication():
    cookie_manager = get_cookie_manager()
    
    # Check if authentication cookie exists
    auth_cookie = cookie_manager.get('auth_token')
    username_cookie = cookie_manager.get('username')
    email_cookie = cookie_manager.get('user_email')
    
    # Initialize session state if not exists
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.username = None
        st.session_state.user_email = None
    
    # If cookies exist but session is not set, restore from cookies
    if auth_cookie and username_cookie and email_cookie and not st.session_state.authenticated:
        st.session_state.authenticated = True
        st.session_state.username = username_cookie
        st.session_state.user_email = email_cookie
    
    # Check if user is authenticated
    if not st.session_state.authenticated:
        st.switch_page("pages/Login.py")
    
    return True

def set_auth_cookies(username, email):
    cookie_manager = get_cookie_manager()
    # Set cookies that expire in 7 days
    expiry = datetime.datetime.now() + datetime.timedelta(days=7)
    
    # Use unique keys for each cookie operation
    cookie_manager.set('auth_token', 'authenticated', expires_at=expiry, key=f"auth_{uuid.uuid4().hex}")
    cookie_manager.set('username', username, expires_at=expiry, key=f"username_{uuid.uuid4().hex}")
    cookie_manager.set('user_email', email, expires_at=expiry, key=f"email_{uuid.uuid4().hex}")

def clear_auth_cookies():
    cookie_manager = get_cookie_manager()
    # Use unique keys for each delete operation
    cookie_manager.delete('auth_token', key=f"del_auth_{uuid.uuid4().hex}")
    cookie_manager.delete('username', key=f"del_username_{uuid.uuid4().hex}")
    cookie_manager.delete('user_email', key=f"del_email_{uuid.uuid4().hex}")

def logout():
    clear_auth_cookies()
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.user_email = None
    st.switch_page("pages/Login.py") 