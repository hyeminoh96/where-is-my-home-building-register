import asyncio
import itertools
import pandas as pd

from src.infrastructure.building_register_repository import BuildingRegisterRepository
from src.infrastructure.register_columns_repository import RegisterColumnsRepository


class BuildingRegisterService:

    @staticmethod
    def get_title_registers(sigungu_code, bjdong_code):
        register_repo = BuildingRegisterRepository()
        registers = asyncio.run(register_repo.async_request_total_registers(sigungu_code, bjdong_code))

        # process with pandas
        flattened_results = list(itertools.chain.from_iterable(registers))
        df = pd.DataFrame.from_records(flattened_results)
        return flattened_results

    def get_columns(self):
        columns_repo = RegisterColumnsRepository()
        columns = columns_repo.query_columns()
        return columns




