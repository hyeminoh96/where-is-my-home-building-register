import requests
import os

from utils import get_request


class BuildingRegister:
    url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo'
    service_key = os.environ.get('API_KEY')

    def __init__(self, sigungu_code, bjdong_code):
        self.sigungu_cd = sigungu_code
        self.bjdong_cd = bjdong_code
        self.num_per_pg = 1000

    def get_total_count(self):
        params = {'_type': 'json', 'serviceKey': self.service_key, 'sigunguCd': self.sigungu_cd,
                  'bjdongCd': self.bjdong_cd,
                  'platGbCd': '0',
                  'bun': '', 'ji': '',
                  'startDate': '', 'endDate': '', 'numOfRows': '1', 'pageNo': '1'}
        response = requests.get(self.url, params=params)
        total_count = response.json()['response']['body']['totalCount']
        return total_count

    def get_bld_rgst(self, page_num):
        params = {'_type': 'json', 'serviceKey': self.service_key, 'sigunguCd': self.sigungu_cd,
                  'bjdongCd': self.bjdong_cd,
                  'platGbCd': '0',
                  'bun': '', 'ji': '',
                  'startDate': '', 'endDate': '', 'numOfRows': self.num_per_pg, 'pageNo': page_num}

        response = get_request(self.url, params)
        response_json = response.json()['response']['body']['items']['item']
        return response_json