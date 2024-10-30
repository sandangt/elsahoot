from app.model import Quiz
from app.viewmodel.core.quiz import QuizVm
from app.viewmodel.core.riddle import RiddleVm
from app.viewmodel.response import QuizResponseVm


def viewmodel_to_model(viewmodel: QuizVm) -> Quiz:
    return Quiz(**viewmodel.model_dump(exclude_unset=True, exclude_none=True))

def model_to_viewmodel(model: Quiz) -> QuizResponseVm:
    quiz_vm = QuizVm.model_validate(model)
    quiz_response_vm = QuizResponseVm(**quiz_vm.model_dump())
    quiz_response_vm.riddles = [RiddleVm.model_validate(riddle) for riddle in model.riddles]
    return quiz_response_vm
