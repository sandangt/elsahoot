from app.repository.player import PlayerRepository
from app.repository.quiz import QuizRepository
from app.repository.riddle import RiddleRepository
from app.resource.db import db_session

player_repository = PlayerRepository(db_session)
quiz_repository = QuizRepository(db_session)
riddle_repository = RiddleRepository(db_session)
