from typing import List

from app.viewmodel.core.player import PlayerVm
from app.viewmodel.core.quiz import QuizVm
from app.viewmodel.core.riddle import RiddleVm


class QuizResponseVm(QuizVm):
    riddles: List[RiddleVm] = []


class PlayerResponseVm(PlayerVm):
    pass
