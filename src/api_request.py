import os
import asyncio

import aiohttp
import requests
from dotenv import load_dotenv


class GetBuildingRegister:
    load_dotenv()
    service_key = os.environ.get('API_KEY')
    bld_rgst_url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo'
    rows_per_page = 1000

    def request_total_count(self, sigungu_cd, bjdong_cd):
        params = {'_type': 'json', 'serviceKey': self.service_key, 'sigunguCd': sigungu_cd,
                  'bjdongCd': bjdong_cd,
                  'platGbCd': '0',
                  'bun': '', 'ji': '',
                  'startDate': '', 'endDate': '', 'numOfRows': '1', 'pageNo': '1'}
        response = requests.get(self.bld_rgst_url, params=params)
        response_json = response.json()
        total_count = response_json['response']['body']['totalCount']
        if total_count == 0:
            raise Exception("건축물대장이 존재하지 않습니다.")
        return total_count

    async def async_request_registers(self, session, page_num, sigungu_cd, bjdong_cd):
        params = {'_type': 'json', 'serviceKey': self.service_key, 'sigunguCd': sigungu_cd,
                  'bjdongCd': bjdong_cd,
                  'platGbCd': '0',
                  'bun': '', 'ji': '',
                  'startDate': '', 'endDate': '', 'numOfRows': self.rows_per_page, 'pageNo': page_num}

        async with session.get(self.bld_rgst_url, params=params) as response:
            response_json = await response.json()
            return response_json['response']['body']['items']['item']

    async def async_request_total_registers(self, sigungu_cd, bjdong_cd):
        total_count = self.request_total_count(sigungu_cd, bjdong_cd)

        if total_count < self.rows_per_page:  # TODO: 중복된 코드 제거
            async with aiohttp.ClientSession() as session:
                task = self.async_request_registers(session, page_num=1, sigungu_cd=sigungu_cd,
                                                    bjdong_cd=bjdong_cd)
                result = await asyncio.gather(task)

        else:
            tasks = []
            async with aiohttp.ClientSession() as session:
                for page in range(1, total_count // self.rows_per_page + 1):
                    task = self.async_request_registers(session, page_num=page, sigungu_cd=sigungu_cd,
                                                        bjdong_cd=bjdong_cd)
                    tasks.append(task)
                result = await asyncio.gather(*tasks)

        return result
