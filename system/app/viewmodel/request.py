from typing import Optional, Tuple, Any
from uuid import UUID

from fastapi import Query
from pydantic import BaseModel, model_serializer
from pydantic.alias_generators import to_snake
from sqlalchemy import desc, asc

from app.constant import DEFAULT_PAGE_SIZE
from app.viewmodel.core.player import PlayerVm
from app.viewmodel.core.quiz import QuizVm


class PaginationParams(BaseModel):
    offset: Optional[int] = Query(None)
    size: Optional[int] = Query(None)

    @model_serializer
    def serialize(self) -> Tuple[int, int]:
        return self.offset or 0, self.size or DEFAULT_PAGE_SIZE


class OrderByParams(BaseModel):
    order: Optional[str] = Query('')

    @model_serializer
    def serialize(self) -> Tuple[Any, str]:
        order_direction, order_by_property = asc, self.order
        if self.order.startswith('-'):
            order_direction = desc
            order_by_property = self.order[1:]
        return order_direction, to_snake(order_by_property)


class CreateQuizVm(QuizVm):
    id: Optional[UUID] = None
    total_score: Optional[int] = None


class CreatePlayerVm(PlayerVm):
    quiz_id: UUID
    id: Optional[str] = None
    score: Optional[int] = 0
    riddles_pass: Optional[int] = 0
