import streamlit as st
import mysql.connector
import io
import pandas as pd

from api_request import getBrTitleInfo


# Initialize connection
@st.experimental_singleton
def init_connection():
    connection = mysql.connector.connect(**st.secrets["mysql"])
    return connection


conn = init_connection()

st.header('Streamlit Test View')


@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


col1, col2, col3, col4 = st.columns(4)
with col1:
    sido_query = "SELECT distinct sido FROM address_code;"
    sido_results = run_query(sido_query)

    sido_list = []
    for _ in sido_results:
        sido_list.append(_[0])

    sido_option = st.selectbox('시도', tuple(sido_list))
    st.write('선택된 시도:', sido_option)

with col2:
    sigungu_query = f"SELECT distinct sigungu FROM address_code WHERE sido='{sido_option}';"
    sigungu_results = run_query(sigungu_query)

    sigungu_list = []
    for _ in sigungu_results:
        sigungu_list.append(_[0])
    sigungu_option = st.selectbox('시군구', tuple(sigungu_list))
    st.write('선택된 시군구:', sigungu_option)

with col3:
    bjdong_query = f"SELECT distinct bjdong FROM address_code WHERE sigungu='{sigungu_option}';"
    bjdong_results = run_query(bjdong_query)

    bjdong_list = []
    for _ in bjdong_results:
        bjdong_list.append(_[0])
    bjdong_option = st.selectbox('동읍면', tuple(bjdong_list))
    st.write('선택된 동읍면:', bjdong_option)

with col4:
    if st.button('조회'):
        address_code_query = f"SELECT sigungucd, bjdongcd FROM address_code WHERE sido = '{sido_option}' AND sigungu = '{sigungu_option}' AND bjdong = '{bjdong_option}'"
        address_code_result = run_query(address_code_query)
        st.write(address_code_result[0])
        sigunguCd = address_code_result[0][0]
        bjdongCd = address_code_result[0][1]
        bld_df = getBrTitleInfo(sigunguCd, bjdongCd, st.secrets['openapi'])

    else:
        st.write('주소를 선택하세요.')

st.dataframe(data=bld_df)

buffer = io.BytesIO()
with pd.ExcelWriter(buffer) as writer:
    bld_df.to_excel(writer)
    writer.save()
    st.download_button(label='📥엑셀로 다운로드', data=buffer, file_name=f"건축물대장_{sido_option}_{sigungu_option}_{bjdong_option}.xlsx",
                       mime='application/vnd.ms-excel')
