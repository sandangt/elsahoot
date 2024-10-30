from sys import prefix

from fastapi import APIRouter
from .quiz import router as quiz_router
from .player import router as player_router
from .testcon import router as testcon_router

router = APIRouter()
router.include_router(quiz_router, prefix='/quizzes', tags=['quizzes'])
router.include_router(player_router, prefix='/players', tags=['players'])
router.include_router(testcon_router, prefix='/test')
