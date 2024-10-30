from fastapi import APIRouter

from app.controller.dependency import PlayerRepositoryDep
from app.exception.custom_exc import ItemNotFoundError
from app.viewmodel.request import CreatePlayerVm
from app.viewmodel.response import PlayerResponseVm
import app.mapper.player as player_mapper

router = APIRouter()

@router.post('/')
async def create(payload: CreatePlayerVm, player_repository: PlayerRepositoryDep) -> PlayerResponseVm:
    payload.id = str(payload.quiz_id) + payload.username
    player = player_mapper.viewmodel_to_model(payload)
    db_player = player_repository.create(player)
    return player_mapper.model_to_viewmodel(
        player_repository.add_quiz(db_player.id, payload.quiz_id)
    )


@router.get('/{player_id}')
async def get_by_id(player_id: str, player_repository: PlayerRepositoryDep) -> PlayerResponseVm:
    db_player = player_repository.get_one_by_id(player_id)
    return player_mapper.model_to_viewmodel(db_player)
