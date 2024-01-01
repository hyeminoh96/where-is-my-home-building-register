from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db import db


class RegisterTitleColumnsMapper(db.Model):
    __tablename__ = 'getBrTitleInfo_mapper'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    kor: Mapped[str] = mapped_column(String(250))
    eng: Mapped[str] = mapped_column(String(250))
    size: Mapped[str] = mapped_column(String(250))
    category: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(250))
    sample: Mapped[str] = mapped_column(String(250))
    status: Mapped[str] = mapped_column(String(250))
