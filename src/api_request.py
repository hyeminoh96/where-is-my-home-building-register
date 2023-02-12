import requests
import pandas as pd
import xmltodict
import os
from time import time
from dotenv import load_dotenv

load_dotenv()
service_key = os.environ.get('API_KEY')
bld_rgst_url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo'


def get_total_count(sigungu_cd, bjdong_cd):
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigungu_cd, 'bjdongCd': bjdong_cd,
              'platGbCd': '0',
              'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': '1', 'pageNo': '1'}
    response = requests.get(bld_rgst_url, params=params)
    total_count = response.json()['response']['body']['totalCount']
    return total_count


def get_bld_rgst(sigungu_cd, bjdong_cd, total_count):
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigungu_cd, 'bjdongCd': bjdong_cd,
              'platGbCd': '0',
              'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': '1000', 'pageNo': '1'}
    result_json = []
    for page_num in range(1, total_count // 1000 + 2):
        print('page_num:', page_num)
        params['pageNo'] = page_num
        response = requests.get(bld_rgst_url, params=params)
        response_json = response.json()['response']['body']['items']['item']
        result_json += response_json
    # result_df = pd.DataFrame(result_json)
    return result_json  # TODO: pandas 처리 분리


def getArchitecturePossessionInfo(sigunguCd, bjdongCd, bld_df, secret):
    service_key = secret['bldrgst_service_key']
    url = 'https://apis.data.go.kr/1611000/OwnerInfoService/getArchitecturePossessionInfo'
    params = {'ServiceKey': service_key, 'sigungu_cd': sigunguCd, 'bjdong_cd': bjdongCd,
              'plat_gb_cd': '0', 'numOfRows': '1000', 'pageNo': '1', 'bun': ''}
    result = []
    for idx, bun in enumerate(bld_df['bun'].unique().tolist()):
        print(f"bun_idx: {idx}/{len(bld_df['bun'].unique().tolist())}")
        params['bun'] = bun
        response = requests.get(url, params=params)
        response_dict = xmltodict.parse(response.content)['response']['body']['items']['item']
        result += response_dict
    result_df = pd.DataFrame(result)
    return result_df


if __name__ == '__main__':
    start = time()
    sigungu_cd = 11230
    bjdong_cd = 10900
    total_count = get_total_count(sigungu_cd, bjdong_cd)
    get_bld_rgst(sigungu_cd, bjdong_cd, total_count)
    end = time()
    print(f'RUN TIME: {end - start}')
