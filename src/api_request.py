import requests
import pandas as pd
import streamlit as st
import mysql.connector


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


def getBrTitleInfo(sigunguCd, bjdongCd, secret):
    service_key = secret['bldrgst_service_key']
    print('service_key:', service_key)
    url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo'
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigunguCd, 'bjdongCd': bjdongCd,
              'platGbCd': '0', 'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': '10', 'pageNo': '1'}

    response = requests.get(url, params=params)
    response_json = response.json()['response']['body']['items']['item']
    response_df = pd.DataFrame(response_json)

    mapping_keys = dict(run_query("SELECT eng, kor FROM response_element_mapper"))
    response_df.rename(columns=mapping_keys, inplace=True)
    return response_df
