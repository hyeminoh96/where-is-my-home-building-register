import mysql.connector
import streamlit as st


@st.experimental_singleton
def init_connection():
    connection = mysql.connector.connect(**st.secrets["mysql"])
    return connection


conn = init_connection()


@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def filter_open_column(df):
    open_col = run_query("SELECT eng FROM response_element_mapper WHERE status = 'open'")
    open_col_list = []
    for _ in open_col:
        open_col_list.append(_[0])

    df = df[open_col_list]

    mapping_keys = dict(run_query("SELECT eng, kor FROM response_element_mapper WHERE status = 'open'"))
    df.rename(columns=mapping_keys, inplace=True)
    return df
