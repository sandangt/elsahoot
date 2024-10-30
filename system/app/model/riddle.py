import uuid
from typing import List

from sqlalchemy import Uuid, ARRAY, String, BigInteger, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.model.base import ElsaBaseModel
from app.model.association import quiz_riddle_association


class Riddle(ElsaBaseModel):
    __tablename__ = 'riddle'
    id = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    title = mapped_column(String, nullable=False, unique=True)
    content = mapped_column(String)
    answer_list = mapped_column(ARRAY(String))
    answer = mapped_column(Integer)

    quizzes: Mapped[List['Quiz']] = relationship(
        secondary=quiz_riddle_association, back_populates='riddles', lazy='dynamic'
    )
