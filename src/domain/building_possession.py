import os
import requests
import xmltodict
import pandas as pd


class BuildingPossession:
    service_key = os.environ.get('API_KEY')
    url = 'https://apis.data.go.kr/1611000/OwnerInfoService/getArchitecturePossessionInfo'

    def get_architecture_possession(self, sigungu_code, bjdong_code, bld_df):

        params = {'ServiceKey': self.service_key, 'sigungu_cd': sigungu_code, 'bjdong_cd': bjdong_code,
                  'plat_gb_cd': '0', 'numOfRows': '1000', 'pageNo': '1', 'bun': ''}
        result = []
        for idx, bun in enumerate(bld_df['bun'].unique().tolist()):
            params['bun'] = bun
            response = requests.get(self.url, params=params)
            response_dict = xmltodict.parse(response.content)['response']['body']['items']['item']
            result += response_dict
        result_df = pd.DataFrame(result)
        return result_df
