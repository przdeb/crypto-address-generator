from __future__ import annotations

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from src.settings.database import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    crypto = Column(String(3))

    @classmethod
    def create(cls, address: str, crypto: str, session: Session) -> Address:
        new_address = cls(address=address, crypto=crypto)
        session.add(new_address)
        session.commit()
        session.refresh(new_address)
        return new_address

    @classmethod
    def get_all(cls, session: Session) -> list:
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, _id: int, session: Session) -> Address:
        return session.query(cls).filter(cls.id == _id).first()
