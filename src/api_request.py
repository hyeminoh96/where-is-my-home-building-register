import requests
import pandas as pd


def getBrTitleInfo(sigunguCd, bjdongCd, secret):
    service_key = secret['bldrgst_service_key']
    url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo'
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigunguCd, 'bjdongCd': bjdongCd,
              'platGbCd': '0',
              # 'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': '2000', 'pageNo': '1'}
    print("params")
    print(params)

    response = requests.get(url, params=params)
    print('response.json()')
    print(response.json())
    response_json = response.json()['response']['body']['items']['item']
    response_df = pd.DataFrame(response_json)
    return response_df
