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


test_query = "SELECT * FROM address_code LIMIT 5;"
rows = run_query(test_query)

# print results
for row in rows:
    st.write(row)
