from src.infrastructure.address_repository import AddressRepository


class AddressService:
    address_repo = AddressRepository()

    def get_sido(self):
        sido_list = self.address_repo.query_sido_list()
        return sido_list

    def get_sigungu(self, sido):
        sigungu_list = self.address_repo.query_sigungu_list(sido)
        return sigungu_list

    def get_bjdong(self, sido, sigungu):
        bjdong_list = self.address_repo.query_bjdong_list(sido, sigungu)
        return bjdong_list

    def get_code(self, sido, sigungu, bjdong):
        pass
