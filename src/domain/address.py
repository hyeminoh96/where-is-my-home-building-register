from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.presentation.flask.app import db


class Address(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sido: Mapped[str] = mapped_column(String)
    sigungu: Mapped[str] = mapped_column(String)
    bjdong: Mapped[str] = mapped_column(String)
    sigungucd: Mapped[int] = mapped_column(Integer)
    bjdongcd: Mapped[int] = mapped_column(Integer)
    note: Mapped[str] = mapped_column(String)
