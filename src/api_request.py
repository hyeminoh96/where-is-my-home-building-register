import requests
import os
import asyncio
from dotenv import load_dotenv

sigungu_cd = 11230
bjdong_cd = 10600

load_dotenv()
service_key = os.environ.get('API_KEY')
bld_rgst_url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo'
num_of_rows = 100

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def get_total_count():
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigungu_cd,
              'bjdongCd': bjdong_cd,
              'platGbCd': '0',
              'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': '1', 'pageNo': '1'}
    response = requests.get(bld_rgst_url, params=params)
    total_count = response.json()['response']['body']['totalCount']
    return total_count


async def fetch_building_register(page_num):
    params = {'_type': 'json', 'serviceKey': service_key, 'sigunguCd': sigungu_cd,
              'bjdongCd': bjdong_cd,
              'platGbCd': '0',
              'bun': '', 'ji': '',
              'startDate': '', 'endDate': '', 'numOfRows': num_of_rows, 'pageNo': page_num}

    response = await loop.run_in_executor(None, requests.get, bld_rgst_url, params)
    response_json = response.json()['response']['body']['items']['item']
    return response_json


async def gather_coroutines(total_count):
    futures = [asyncio.ensure_future(fetch_building_register(pg_num)) for pg_num in
               range(1, total_count // num_of_rows + 2)]
    result = await asyncio.gather(*futures)
    print("RESULT:", result)
    print('TOTAL COUNT:', total_count)
    print("LEN:", len(result))
    print("LEN[0]:", len(result[0]))
    print("LEN[:-1]:", len(result[:-1]))

    return result


if __name__ == '__main__':
    total_count = get_total_count()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather_coroutines(total_count))
    loop.close()
