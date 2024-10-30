from typing import Annotated

from fastapi import Depends

from app.controller.dependency.crud import get_player_repository, get_quiz_repository, get_riddle_repository
from app.controller.dependency.ws import get_ws_handler
from app.repository import PlayerRepository, QuizRepository, RiddleRepository
from app.resource.wshandler import WSHandler

PlayerRepositoryDep = Annotated[PlayerRepository, Depends(get_player_repository)]
QuizRepositoryDep = Annotated[QuizRepository, Depends(get_quiz_repository)]
RiddleRepositoryDep = Annotated[RiddleRepository, Depends(get_riddle_repository)]
WSHandlerDep = Annotated[WSHandler, Depends(get_ws_handler)]
