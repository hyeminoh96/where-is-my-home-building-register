import requests
import pandas as pd


def getBrTitleInfo(sigunguCd, bjdongCd, secret):
    service_key = secret['bldrgst_service_key']
    url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo'
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigunguCd, 'bjdongCd': bjdongCd,
              'platGbCd': '0',
              'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': '1000', 'pageNo': '1'}
    print("params")
    print(params)
    response = requests.get(url, params=params)
    total_count = response.json()['response']['body']['totalCount']
    print('total_count:', total_count)
    result_json = []
    for page_num in range(1, total_count // 1000 + 2):
        params['pageNo'] = page_num
        response = requests.get(url, params=params)
        response_json = response.json()['response']['body']['items']['item']
        result_json += response_json
    result_df = pd.DataFrame(result_json)
    return result_df
