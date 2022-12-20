import streamlit as st
import io
import pandas as pd

from api_request import getBrTitleInfo
from db import filter_open_column, get_sido_list, get_sigungu_list, get_bjdong_list, get_address_code


col1, col2, col3, col4 = st.columns(4)
with col1:
    sido_list = get_sido_list()
    sido_option = st.selectbox('시도', tuple(sido_list))
    st.write('선택된 시도:', sido_option)

with col2:
    sigungu_list = get_sigungu_list(sido_option)
    sigungu_option = st.selectbox('시군구', tuple(sigungu_list))
    st.write('선택된 시군구:', sigungu_option)

with col3:
    bjdong_list = get_bjdong_list(sigungu_option)
    bjdong_option = st.selectbox('동읍면', tuple(bjdong_list))
    st.write('선택된 동읍면:', bjdong_option)

with col4:
    if st.button('조회'):
        sigungu_code, bjdong_code = get_address_code(sido_option, sigungu_option, bjdong_option)
        bld_df = getBrTitleInfo(sigungu_code, bjdong_code, st.secrets['openapi'])
        bld_df = filter_open_column(bld_df)

    else:
        st.write('주소를 선택하세요.')

st.dataframe(data=bld_df)

buffer = io.BytesIO()
with pd.ExcelWriter(buffer) as writer:
    bld_df.to_excel(writer)
    writer.save()
    st.download_button(label='📥엑셀로 다운로드', data=buffer,
                       file_name=f"건축물대장_{sido_option}_{sigungu_option}_{bjdong_option}.xlsx",
                       mime='application/vnd.ms-excel')
