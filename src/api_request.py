import requests
import pandas as pd
import xmltodict


def getBrTitleInfo(sigunguCd, bjdongCd, secret):
    service_key = secret['bldrgst_service_key']
    url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo'
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigunguCd, 'bjdongCd': bjdongCd,
              'platGbCd': '0',
              'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': '1000', 'pageNo': '1'}  # FIXME
    print("params")
    print(params)
    response = requests.get(url, params=params)
    total_count = response.json()['response']['body']['totalCount']
    print('total_count:', total_count)
    result_json = []
    for page_num in range(1, total_count // 1000 + 2):  # FIXME
        # for page_num in range(1, 2):
        print('page_num:', page_num)
        params['pageNo'] = page_num
        response = requests.get(url, params=params)
        response_json = response.json()['response']['body']['items']['item']
        result_json += response_json
    result_df = pd.DataFrame(result_json)
    return result_df


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
