import uuid
from typing import List, Set

from sqlalchemy import Uuid, String, BigInteger
from sqlalchemy.orm import mapped_column, relationship, Mapped

from app.model.base import ElsaBaseModel
from app.model.association import quiz_riddle_association


class Quiz(ElsaBaseModel):
    __tablename__ = 'quiz'
    id = mapped_column(Uuid, primary_key=True, default=uuid.uuid1)
    topic = mapped_column(String)
    total_score = mapped_column(BigInteger)

    players: Mapped[List['Player']] = relationship(back_populates='quiz', lazy='joined')

    riddles: Mapped[Set['Riddle']] = relationship(secondary=quiz_riddle_association,
                                                  back_populates='quizzes', lazy='joined')
