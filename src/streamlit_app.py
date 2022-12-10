import streamlit as st
import mysql.connector


# Initialize connection
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])


conn = init_connection()

st.header('Streamlit Test View')


@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


rows = run_query("SELECT * FROM address_code limit 5;")

# print results
for row in rows:
    st.write(row)
