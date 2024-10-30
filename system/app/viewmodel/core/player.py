from app.viewmodel.core.base import ElsaBaseEntity


class PlayerVm(ElsaBaseEntity):
    id: str
    username: str
    score: int
    riddles_pass: int
