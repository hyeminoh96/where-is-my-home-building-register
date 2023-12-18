from dataclasses import dataclass

from typing import List

from src.domain.building_register_columns_info import RegisterTitleColumnsMapper
from src.infrastructure.db import db


@dataclass
class RegisterTitleColumns:
    eng: str
    kor: str


class RegisterColumnsRepository:
    def query_columns(self) -> List[RegisterTitleColumns]:
        result = db.session.execute(
            db.select(RegisterTitleColumnsMapper.eng, RegisterTitleColumnsMapper.kor).filter_by(
                status='open')).all()
        result = [RegisterTitleColumns(eng=row[0], kor=row[1]) for row in result]
        return result
