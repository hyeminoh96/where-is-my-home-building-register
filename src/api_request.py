import requests
import pandas as pd


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
    return response_df
