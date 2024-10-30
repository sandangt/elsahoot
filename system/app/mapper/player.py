from app.model import Player
from app.viewmodel.core.player import PlayerVm
from app.viewmodel.response import PlayerResponseVm


def viewmodel_to_model(viewmodel: PlayerVm) -> Player:
    return Player(**viewmodel.model_dump(exclude_none=True))

def model_to_viewmodel(model: Player) -> PlayerResponseVm:
    player_vm = PlayerVm.model_validate(model)
    player_response_vm = PlayerResponseVm(**player_vm.model_dump())
    return player_response_vm
