import sqlite3
import bcrypt
import streamlit as st
import uuid
from datetime import datetime

DB_PATH = '/Users/zafer/Documents/GitHub/salesense/database/database.sqlite'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def login(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode(), user["password"]):
        session_id = str(uuid.uuid4())
        st.session_state['session_id'] = session_id
        st.session_state['user_id'] = user['id']
        st.session_state['username'] = user['username']
        st.session_state['email'] = user['email']

        save_session(user['id'], session_id)
        return True

    return False

def save_session(user_id, session_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Aynı user için önceden oluşturulmuş session varsa sil (isteğe bağlı)
    cursor.execute("DELETE FROM sessions WHERE user_id = ?", (user_id,))

    cursor.execute("INSERT INTO sessions (user_id, session_id) VALUES (?, ?)", (user_id, session_id))
    conn.commit()
    conn.close()

def check_session():
    if 'session_id' not in st.session_state or 'user_id' not in st.session_state:
        return False

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions WHERE user_id = ? AND session_id = ?", 
                   (st.session_state['user_id'], st.session_state['session_id']))
    session = cursor.fetchone()
    conn.close()

    return session is not None

def logout():
    if 'session_id' in st.session_state and 'user_id' in st.session_state:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sessions WHERE user_id = ? AND session_id = ?", 
                       (st.session_state['user_id'], st.session_state['session_id']))
        conn.commit()
        conn.close()

    for key in ['session_id', 'user_id', 'username']:
        if key in st.session_state:
            del st.session_state[key]
