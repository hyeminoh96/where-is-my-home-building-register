from src.infrastructure.building_register_repository import BuildingRegisterRepository


class BuildingRegisterService:

    @staticmethod
    async def get_title_registers(sigungu_code, bjdong_code):
        register_repo = BuildingRegisterRepository()
        registers = await register_repo.async_request_total_registers(sigungu_code, bjdong_code)
        return registers
