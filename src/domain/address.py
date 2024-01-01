from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db import db


class Address(db.Model):
    __tablename__ = 'address_code'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sido: Mapped[str] = mapped_column(String(250))
    sigungu: Mapped[str] = mapped_column(String(250))
    bjdong: Mapped[str] = mapped_column(String(250))
    sigungucd: Mapped[int] = mapped_column(Integer)
    bjdongcd: Mapped[int] = mapped_column(Integer)
    note: Mapped[str] = mapped_column(String(250))
