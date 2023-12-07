from src.domain.building_register_columns_info import RegisterTitleColumnsMapper
from src.infrastructure.db import db


class RegisterColumnsRepository:
    def query_columns(self):
        result = db.session.execute(
            db.select(RegisterTitleColumnsMapper.eng, RegisterTitleColumnsMapper.kor).filter_by(
                status='open')).all()

        return result
