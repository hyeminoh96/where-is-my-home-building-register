import streamlit as st
import mysql.connector


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


sido_query = "SELECT distinct sido FROM address_code;"
sido_results = run_query(sido_query)

# results to tuple
sido_list = []
for _ in sido_results:
    sido_list.append(_[0])

sido_option = st.selectbox('시도', tuple(sido_list))
st.write('선택된 시도:', sido_option)

sigungu_query = f"SELECT distinct sigungu FROM address_code WHERE sido='{sido_option}';"
print('sigungu_query:', sigungu_query)
sigungu_results = run_query(sigungu_query)

print('sigungu_results:', sigungu_results)
