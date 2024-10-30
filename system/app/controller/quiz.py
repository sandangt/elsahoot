import random
from uuid import UUID

from fastapi import APIRouter

from app.constant import RIDDLES_PER_QUIZ, SCORE_PER_RIDDLE
from app.controller.dependency import QuizRepositoryDep, RiddleRepositoryDep
from app.viewmodel.request import CreateQuizVm, PaginationParams, OrderByParams
from app.mapper import quiz as quiz_mapper
from app.viewmodel.response import QuizResponseVm

router = APIRouter()

@router.post('/')
async def create(payload: CreateQuizVm,
                quiz_repository: QuizRepositoryDep,
                riddle_repository: RiddleRepositoryDep) -> QuizResponseVm:
    if not payload.total_score:
        payload.total_score = RIDDLES_PER_QUIZ * SCORE_PER_RIDDLE
    quiz = quiz_mapper.viewmodel_to_model(payload)
    db_quiz = quiz_repository.create(quiz)
    riddle_count = riddle_repository.count()
    pagination = PaginationParams(offset=random.randint(0, riddle_count / RIDDLES_PER_QUIZ), size=RIDDLES_PER_QUIZ)
    order_by = OrderByParams(order='-created_on')
    riddle_ids = [i.id for i in riddle_repository.get_all_paginated(pagination, order_by)]
    return quiz_mapper.model_to_viewmodel(
        quiz_repository.add_all_riddles(db_quiz.id, riddle_ids)
    )

@router.get('/{quiz_id}')
async def get_by_id(quiz_id: UUID, quiz_repository: QuizRepositoryDep) -> QuizResponseVm:
    quiz = quiz_repository.get_one_by_id(quiz_id)
    return quiz_mapper.model_to_viewmodel(quiz)
