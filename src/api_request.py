import requests
import pandas as pd


def getBrTitleInfo(sigunguCd, bjdongCd, secret):
    serviceKey = secret['bldrgst_service_key']
    print('serviceKey:', serviceKey)
    url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo'
    params = {'_type': 'json', 'serviceKey': serviceKey, 'sigunguCd': sigunguCd, 'bjdongCd': bjdongCd,
              'platGbCd': '0', 'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': '10', 'pageNo': '1'}

    response = requests.get(url, params=params)
    return response.json()['response']['body']['items']['item']
