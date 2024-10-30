from app.model import Riddle
from app.repository.crud import CRUDRepository


class RiddleRepository(CRUDRepository[Riddle]):
    _model_type = Riddle
