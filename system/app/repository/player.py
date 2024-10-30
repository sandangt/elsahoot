from typing import Type, Optional
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from app.model import Player, Quiz
from .crud import CRUDRepository
from ..exception.custom_exc import ItemNotFoundError


class PlayerRepository(CRUDRepository[Player]):
    _model_type = Player

    def add_quiz(self, item_id: str, quiz_id: UUID) -> Type[Player]:
        with self._db_session.begin() as session:
            if not (item := session.get(self._model_type, item_id)):
                raise ItemNotFoundError('Player not found')
            quiz = session.get(Quiz, quiz_id)
            try:
                item.quiz = quiz
                session.commit()
            except SQLAlchemyError as exc:
                session.rollback()
                raise exc
        with self._db_session.begin() as session:
            updated_item = session.get(self._model_type, item_id)
            session.expunge_all()
        return updated_item

    def get_one_by_username(self, username: str) -> Optional[Player]:
        with self._db_session.begin() as session:
            item = session.query(self._model_type).filter_by(username=username).first()
            if not item:
                raise ItemNotFoundError('Player not found')
            session.expunge(item)
        return item
