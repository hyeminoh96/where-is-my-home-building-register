import mysql.connector
import streamlit as st


@st.cache_resource
def init_connection():
    connection = mysql.connector.connect(**st.secrets["mysql"])
    return connection


conn = init_connection()


@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_sido_list():
    sido_query = "SELECT distinct sido FROM address_code;"
    sido_results = run_query(sido_query)

    sido_list = []
    for _ in sido_results:
        sido_list.append(_[0])
    return sido_list


def get_sigungu_list(sido_option):
    sigungu_query = f"SELECT distinct sigungu FROM address_code WHERE sido='{sido_option}';"
    sigungu_results = run_query(sigungu_query)

    sigungu_list = []
    for _ in sigungu_results:
        sigungu_list.append(_[0])
    return sigungu_list


def get_bjdong_list(sigungu_option):
    bjdong_query = f"SELECT distinct bjdong FROM address_code WHERE sigungu='{sigungu_option}';"
    bjdong_results = run_query(bjdong_query)

    bjdong_list = []
    for _ in bjdong_results:
        bjdong_list.append(_[0])
    return bjdong_list


def get_address_code(sido_option, sigungu_option, bjdong_option):
    address_code_query = f"SELECT sigungucd, bjdongcd FROM address_code WHERE sido = '{sido_option}' AND sigungu = '{sigungu_option}' AND bjdong = '{bjdong_option}'"
    address_code_result = run_query(address_code_query)
    sigungu_code = address_code_result[0][0]
    bjdong_code = address_code_result[0][1]
    return sigungu_code, bjdong_code


def filter_open_column(df):
    open_col = run_query("SELECT eng FROM getBrExposInfo_mapper WHERE status = 'open'")
    open_col_list = []
    for _ in open_col:
        open_col_list.append(_[0])

    df = df[open_col_list]

    mapping_keys = dict(run_query("SELECT eng, kor FROM getBrExposInfo_mapper WHERE status = 'open'"))
    df.rename(columns=mapping_keys, inplace=True)
    return df


def filter_owner_open_column(df):
    open_col = run_query("SELECT eng FROM getArchitecturePossessionInfo_mapper WHERE status = 'open'")
    open_col_list = []
    for _ in open_col:
        open_col_list.append(_[0])
    df = df[open_col_list]
    mapping_keys = dict(run_query("SELECT eng, kor FROM getArchitecturePossessionInfo_mapper WHERE status = 'open'"))
    df.rename(columns=mapping_keys, inplace=True)
    return df
