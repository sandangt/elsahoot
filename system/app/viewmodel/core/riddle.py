from typing import List
from uuid import UUID

from app.viewmodel.core.base import ElsaBaseEntity


class RiddleVm(ElsaBaseEntity):
    id: UUID
    title: str
    content: str
    answer_list: List[str] = []
    answer: int
