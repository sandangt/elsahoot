from app.repository import PlayerRepository, player_repository, quiz_repository, QuizRepository, RiddleRepository, \
    riddle_repository


def get_player_repository() -> PlayerRepository:
    return player_repository

def get_quiz_repository() -> QuizRepository:
    return quiz_repository

def get_riddle_repository() -> RiddleRepository:
    return riddle_repository
