import os
import requests
import xmltodict
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
service_key = os.environ.get('API_KEY')


def getArchitecturePossessionInfo(sigunguCd, bjdongCd, bld_df, secret):
    service_key = secret['bldrgst_service_key']
    url = 'https://apis.data.go.kr/1611000/OwnerInfoService/getArchitecturePossessionInfo'
    params = {'ServiceKey': service_key, 'sigungu_cd': sigunguCd, 'bjdong_cd': bjdongCd,
              'plat_gb_cd': '0', 'numOfRows': '1000', 'pageNo': '1', 'bun': ''}
    result = []
    for idx, bun in enumerate(bld_df['bun'].unique().tolist()):
        print(f"bun_idx: {idx}/{len(bld_df['bun'].unique().tolist())}")
        params['bun'] = bun
        response = requests.get(url, params=params)
        response_dict = xmltodict.parse(response.content)['response']['body']['items']['item']
        result += response_dict
    result_df = pd.DataFrame(result)
    return result_df
