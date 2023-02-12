import requests
import os
import asyncio
from time import time
from dotenv import load_dotenv

load_dotenv()
service_key = os.environ.get('API_KEY')
bld_rgst_url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo'
num_per_pg = 1000


def get_total_count(sigungu_cd, bjdong_cd):
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigungu_cd, 'bjdongCd': bjdong_cd,
              'platGbCd': '0',
              'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': '1', 'pageNo': '1'}
    response = requests.get(bld_rgst_url, params=params)
    total_count = response.json()['response']['body']['totalCount']
    return total_count


async def get_bld_rgst(sigungu_cd, bjdong_cd, page_num):
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigungu_cd, 'bjdongCd': bjdong_cd,
              'platGbCd': '0',
              'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': num_per_pg, 'pageNo': page_num}

    response = await loop.run_in_executor(None, requests.get, bld_rgst_url, params)
    response_json = response.json()['response']['body']['items']['item']
    return response_json  # TODO: pandas 처리 분리


async def gather_coroutines():
    total_count = get_total_count(sigungu_cd, bjdong_cd)
    futures = [asyncio.ensure_future(get_bld_rgst(sigungu_cd, bjdong_cd, pg_num)) for pg_num in
               range(1, total_count // num_per_pg + 2)]

    result = await asyncio.gather(*futures)
    return result


if __name__ == '__main__':
    start = time()
    sigungu_cd = 11230
    bjdong_cd = 10900

    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather_coroutines())
    loop.close()

    end = time()
    print(f'RUN TIME: {end - start}')
