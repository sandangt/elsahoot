package elsahoot.console.controller;

import elsahoot.console.dto.extended.QuizExtendedDto;
import elsahoot.console.exception.ItemNotFoundException;
import elsahoot.console.mapper.IQuizMapper;
import elsahoot.console.mapper.IRiddleMapper;
import elsahoot.console.model.Quiz;
import elsahoot.console.model.QuizRiddleAssociate;
import elsahoot.console.repository.crud.IQuizRepository;
import elsahoot.console.repository.crud.IQuizRiddleRepository;
import elsahoot.console.repository.crud.IRiddleRepository;
import lombok.RequiredArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/quizzes")
@RequiredArgsConstructor
public class QuizController {

    private final IQuizRepository quizRepository;
    private final IRiddleRepository riddleRepository;
    private final IQuizRiddleRepository quizRiddleRepository;
    private final IQuizMapper quizMapper;
    private final IRiddleMapper riddleMapper;

    @GetMapping("/{id}")
    public ResponseEntity<QuizExtendedDto> getQuizById(@PathVariable ObjectId id) {
        Quiz quiz = quizRepository.findById(id)
            .orElseThrow(() -> new ItemNotFoundException("Quiz not found"));
        var quizRiddles = quizRiddleRepository.findAllByQuizIdIn(List.of(quiz.getId()));
        var riddleList = riddleRepository.findAllByIdIn(
            quizRiddles.stream().map(QuizRiddleAssociate::getRiddleId).toList());
        var quizDto = quizMapper.entityToExtendedDto(quiz);
        quizDto.setRiddles(riddleMapper.entityToDto(riddleList));
        return ResponseEntity.ok(quizDto);
    }

}
