from src.domain.address import Address
from src.infrastructure.db import db


class AddressRepository:
    def query_sido_list(self) -> dict:
        result = db.session.execute(db.select(Address.sido).distinct()).all()
        result = [_tup[0] for _tup in result]
        return {"sido": result}

    def query_sigungu_list(self, sido) -> dict:
        result = db.session.execute(db.select(Address.sigungu).distinct().filter_by(sido=sido)).all()
        result = [_tup[0] for _tup in result]
        return {"sigungu": result}

    def query_bjdong_list(self, sido, sigungu) -> dict:
        result = db.session.execute(db.select(Address.bjdong).filter_by(sido=sido).filter_by(sigungu=sigungu)).all()
        result = [_tup[0] for _tup in result]
        return {"bjdong": result}

    def query_code(self, sido, sigungu, bjdong) -> dict:
        sigungu_code, bjdong_code = db.session.execute(
            db.select(Address.sigungucd, Address.bjdongcd).filter_by(sido=sido).filter_by(sigungu=sigungu).filter_by(
                bjdong=bjdong)).one()

        return {"sigungu_code": sigungu_code, "bjdong_code": bjdong_code}
