from src.infrastructure.building_register_repository import BuildingRegisterRepository


class BuildingRegisterService:
    register_repo = BuildingRegisterRepository()

    def get_general_registers(self, sigungu_code, bjdong_code):
        self.register_repo.request_total_registers(sigungu_code, bjdong_code)


