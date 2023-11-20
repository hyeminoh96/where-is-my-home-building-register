from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class Address(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sido: Mapped[str] = mapped_column(String(250))
    sigungu: Mapped[str] = mapped_column(String(250))
    bjdong: Mapped[str] = mapped_column(String(250))
    sigungucd: Mapped[int] = mapped_column(Integer)
    bjdongcd: Mapped[int] = mapped_column(Integer)
    note: Mapped[str] = mapped_column(String(250))
