from typing import Optional

from sqlalchemy import String, ForeignKey, Integer, BigInteger
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.model.base import ElsaBaseModel


class Player(ElsaBaseModel):
    __tablename__ = 'player'
    id = mapped_column(String, primary_key=True)
    username = mapped_column(String, nullable=False, unique=True)
    score = mapped_column(BigInteger)
    riddles_pass = mapped_column(Integer)

    quiz_id = mapped_column(ForeignKey('quiz.id'))
    quiz: Mapped[Optional['Quiz']] = relationship(back_populates='players')
