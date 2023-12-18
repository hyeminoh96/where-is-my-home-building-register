import asyncio
import itertools
from dataclasses import dataclass
from typing import List

import pandas as pd

from src.infrastructure.building_register_repository import BuildingRegisterRepository
from src.infrastructure.register_columns_repository import RegisterColumnsRepository, RegisterTitleColumns


@dataclass
class RegisterTitleColumnsResponse:
    columns: List[RegisterTitleColumns]


class BuildingRegisterService:

    @staticmethod
    def get_title_registers(sigungu_code, bjdong_code, columns):
        register_repo = BuildingRegisterRepository()
        registers = asyncio.run(register_repo.async_request_total_registers(sigungu_code, bjdong_code))

        flattened_results = list(itertools.chain.from_iterable(registers))
        df = pd.DataFrame.from_records(flattened_results)

        columns_code = [column['eng'] for column in columns]
        df = df[columns_code]

        # Rename columns in Korean
        mapped_columns = {columns['eng']: columns['kor'] for columns in columns}

        df.rename(columns=mapped_columns, inplace=True)

        return df.to_json(orient='records', force_ascii=False)

    def get_columns(self):
        columns_repo = RegisterColumnsRepository()
        columns = columns_repo.query_columns()

        return RegisterTitleColumnsResponse(columns=columns)
