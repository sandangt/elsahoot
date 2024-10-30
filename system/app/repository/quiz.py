from typing import List, Type
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from app.exception.custom_exc import ItemNotFoundError
from app.model import Quiz, Riddle
from app.repository.crud import CRUDRepository


class QuizRepository(CRUDRepository[Quiz]):
    _model_type = Quiz

    def add_all_riddles(self, item_id: UUID, riddle_ids: List[UUID]) -> Type[Quiz]:
        with self._db_session.begin() as session:
            if not (item := session.get(self._model_type, item_id)):
                raise ItemNotFoundError('Quiz not found')
            riddles = session.query(Riddle).filter(Riddle.id.in_(riddle_ids)).all()
            try:
                item.riddles = set(riddles)
                session.commit()
            except SQLAlchemyError as ex:
                session.rollback()
                raise ex
        with self._db_session.begin() as session:
            updated_item = session.get(self._model_type, item_id)
            session.expunge_all()
        return updated_item
