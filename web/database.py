import pandas as pd
import sqlite3

DATABASE = "/Users/zafer/Documents/GitHub/salesense/database/database.sqlite" 

def query_db(query):
    conn = sqlite3.connect(DATABASE)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def insert_db(query):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    return True

def update_db(query):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    return True

