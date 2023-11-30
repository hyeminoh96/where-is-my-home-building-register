import os

from src.infrastructure.utils import get_request


class BuildingRegisterRepository:
    url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrRecapTitleInfo'  # 총괄표제부 url
    service_key = os.environ.get('API_KEY')
    rows_per_page = 1000

    def request_total_count(self, sigungu_cd, bjdong_cd):
        params = {'_type': 'json', 'serviceKey': self.service_key, 'sigunguCd': str(sigungu_cd),
                  'bjdongCd': str(bjdong_cd),
                  'platGbCd': '0',
                  'bun': '', 'ji': '',
                  'startDate': '', 'endDate': '', 'numOfRows': '1', 'pageNo': '1'}
        response = get_request(self.url, params=params)
        response_json = response.json()
        total_count = response_json['response']['body']['totalCount']
        if total_count == 0:
            print("건축물대장이 존재하지 않습니다.")
        return total_count

    def request_registers(self, page_num, sigungu_cd, bjdong_cd):
        params = {'_type': 'json', 'serviceKey': self.service_key, 'sigunguCd': sigungu_cd,
                  'bjdongCd': bjdong_cd,
                  'platGbCd': '0',
                  'bun': '', 'ji': '',
                  'startDate': '', 'endDate': '', 'numOfRows': self.rows_per_page, 'pageNo': page_num}

        response = get_request(self.url, params)
        response_json = response.json()['response']['body']['items']['item']
        return response_json

    def request_total_registers(self, sigungu_cd, bjdong_cd):
        result = []
        total_count = self.request_total_count(sigungu_cd, bjdong_cd)

        if total_count < self.rows_per_page:
            registers = self.request_registers(page_num=1, sigungu_cd=sigungu_cd, bjdong_cd=bjdong_cd)
            result += registers
        else:
            for page in range(1, total_count // self.rows_per_page + 1):
                registers = self.request_registers(page_num=page, sigungu_cd=sigungu_cd, bjdong_cd=bjdong_cd)
                result += registers

        return result
