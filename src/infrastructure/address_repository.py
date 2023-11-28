from src.domain.address import Address
from src.infrastructure.db import db


class AddressRepository:
    def query_sido_list(self) -> list:
        result = db.session.execute(db.select(Address.sido).distinct()).scalars()
        return result

    def query_sigungu_list(self, sido) -> list:
        result = db.session.execute(db.select(Address.sigungu).distinct().filter_by(sido=sido)).scalars()
        return result

    def query_bjdong_list(self, sido, sigungu) -> list:
        result = db.session.execute(db.select(Address.bjdong).filter_by(sido=sido).filter_by(sigungu=sigungu)).scalars()
        return result
