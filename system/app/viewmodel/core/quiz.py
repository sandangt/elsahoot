from uuid import UUID

from app.viewmodel.core.base import ElsaBaseEntity


class QuizVm(ElsaBaseEntity):
    id: UUID
    topic: str
    total_score: int
