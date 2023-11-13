import streamlit as st
import io
import pandas as pd

from src.infrastructure.db import filter_open_column, get_sido_list, get_sigungu_list, get_bjdong_list, get_address_code, \
    filter_owner_open_column
from src.domain.building_register import BuildingRegister

st.header('🏡 건축물대장 조회')

col1, col2, col3, col4 = st.columns(4)
with col1:
    sido_list = get_sido_list()
    sido_option = st.selectbox('시도', tuple(sido_list))

with col2:
    sigungu_list = get_sigungu_list(sido_option)
    sigungu_option = st.selectbox('시군구', tuple(sigungu_list))

with col3:
    bjdong_list = get_bjdong_list(sigungu_option)
    bjdong_option = st.selectbox('동읍면', tuple(bjdong_list))

with col4:
    search_button = st.button('조회')

if search_button:
    sigungu_code, bjdong_code = get_address_code(sido_option, sigungu_option, bjdong_option)
    bld_df = BuildingRegister(sigungu_code, bjdong_code).run()
    owner_df = bld_df.get_architecture_possession(sigungu_code, bjdong_code, bld_df, st.secrets['openapi'])
    bld_df = filter_open_column(bld_df)
    owner_df = filter_owner_open_column(owner_df)
    total_df = pd.merge(left=bld_df, right=owner_df, how='left', on='건축물대장번호')
    st.dataframe(total_df)

    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        total_df.to_excel(writer, index=False)
        writer.save()
        st.download_button(label='📥엑셀로 다운로드', data=buffer,
                           file_name=f"건축물대장_{sido_option}_{sigungu_option}_{bjdong_option}.xlsx",
                           mime='application/vnd.ms-excel')
        st.success("다운로드가 완료되었습니다.", icon="✅")

