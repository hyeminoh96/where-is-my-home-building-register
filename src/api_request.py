import requests
import os
import asyncio
from time import time
from dotenv import load_dotenv


class GetBuildingRegister:
    def __init__(self, sigungu_code, bjdong_code):
        self.sigungu_cd = sigungu_code
        self.bjdong_cd = bjdong_code

        load_dotenv()
        self.service_key = os.environ.get('API_KEY')
        self.bld_rgst_url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo'
        self.num_per_pg = 1000

        self.loop = asyncio.get_event_loop()

    def get_total_count(self):
        params = {'_type': 'json', 'serviceKey': self.service_key, 'sigunguCd': self.sigungu_cd,
                  'bjdongCd': self.bjdong_cd,
                  'platGbCd': '0',
                  'bun': '', 'ji': '',
                  'startDate': '', 'endDate': '', 'numOfRows': '1', 'pageNo': '1'}
        response = requests.get(self.bld_rgst_url, params=params)
        total_count = response.json()['response']['body']['totalCount']
        return total_count

    async def get_bld_rgst(self, page_num):
        params = {'_type': 'json', 'serviceKey': self.service_key, 'sigunguCd': self.sigungu_cd,
                  'bjdongCd': self.bjdong_cd,
                  'platGbCd': '0',
                  'bun': '', 'ji': '',
                  'startDate': '', 'endDate': '', 'numOfRows': self.num_per_pg, 'pageNo': page_num}

        response = await self.loop.run_in_executor(None, requests.get, self.bld_rgst_url, params)
        response_json = response.json()['response']['body']['items']['item']
        return response_json

    async def gather_coroutines(self):
        total_count = self.get_total_count()
        futures = [asyncio.ensure_future(self.get_bld_rgst(pg_num)) for pg_num in
                   range(1, total_count // self.num_per_pg + 2)]
        result = await asyncio.gather(*futures)
        return result

    def run(self):
        self.loop.run_until_complete(self.gather_coroutines())
        self.loop.close()


if __name__ == '__main__':
    start = time()
    GetBuildingRegister(11230, 10900).run()
    end = time()
    print(f'RUN TIME: {end - start}')
