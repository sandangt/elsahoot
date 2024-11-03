package elsahoot.console.service;

import com.github.javafaker.Faker;
import elsahoot.console.model.Quiz;
import elsahoot.console.model.QuizRiddleAssociate;
import elsahoot.console.model.Riddle;
import elsahoot.console.repository.crud.IQuizRepository;
import elsahoot.console.repository.crud.IQuizRiddleRepository;
import elsahoot.console.repository.crud.IRiddleRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Bean;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.stream.IntStream;

import static elsahoot.console.constant.AppNumber.DEFAULT_RIDDLE_PER_QUIZ;
import static elsahoot.console.constant.AppNumber.DEFAULT_SCORE_PER_QUIZ;

@Service
@Slf4j
@RequiredArgsConstructor
public class FakeService {

    private final IQuizRepository quizRepository;
    private final IRiddleRepository riddleRepository;
    private final IQuizRiddleRepository quizRiddleRepository;

    @Bean
    public Faker getFaker() {
        return new Faker();
    }

    public void seedRiddle(int number) {
        if (riddleRepository.count() > 0) return;
        var faker = getFaker();

        var result = IntStream.range(0, number).mapToObj(ignore -> {
            int titleWordNumber = faker.number().numberBetween(5, 15);
            int contentSentenceNumber = faker.number().numberBetween(7, 20);
            int numberOfAnswer = faker.number().numberBetween(4, 10);
            int correctAnswerNumber = faker.number().numberBetween(0, numberOfAnswer - 1);
            faker.funnyName().name();
            return Riddle.builder()
                .title(faker.lorem().sentence(titleWordNumber))
                .content(faker.lorem().paragraph(contentSentenceNumber))
                .answer(correctAnswerNumber)
                .answerList(faker.lorem().sentences(numberOfAnswer))
                .build();
        }).toList();
        riddleRepository.saveAll(result);
    }

    public void seedQuiz(int number) {
        if (quizRepository.count() > 0) return;
        long totalRiddles = riddleRepository.count();
        var faker = getFaker();
        List<QuizRiddleAssociate> quizRiddleList = new LinkedList<>();

        for (int i=0; i<number; i++) {
            int riddlesPerQuiz = faker.number().numberBetween(75, 150);
            int randomPageNumber = faker.number().numberBetween(0, (int) (totalRiddles / riddlesPerQuiz));
            Pageable pageRequest = PageRequest
                .of(randomPageNumber, riddlesPerQuiz, Sort.by("createdAt").descending());
            int totalScore = riddlesPerQuiz * DEFAULT_RIDDLE_PER_QUIZ;
            Quiz dbQuiz = quizRepository.save(Quiz.builder()
                .topic(faker.funnyName().name())
                .totalScore((long) totalScore)
                .build());
            Page<Riddle> riddleList = riddleRepository.findAll(pageRequest);
            quizRiddleList.addAll(riddleList.stream().map(riddle ->
                QuizRiddleAssociate.builder()
                    .quizId(dbQuiz.getId())
                    .riddleId(riddle.getId())
                    .build())
                .toList());
        }
        quizRiddleRepository.saveAll(quizRiddleList);
    }

}
