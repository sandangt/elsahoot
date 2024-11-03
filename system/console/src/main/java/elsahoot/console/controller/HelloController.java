package elsahoot.console.controller;

import elsahoot.console.dto.core.PlayerDto;
import elsahoot.console.exception.ItemNotFoundException;
import elsahoot.console.mapper.IPlayerMapper;
import elsahoot.console.mapper.IQuizMapper;
import elsahoot.console.model.Player;
import elsahoot.console.repository.crud.IPlayerRepository;
import elsahoot.console.repository.crud.IQuizRepository;
import elsahoot.console.viewmodel.request.EnterPlaygroundRequest;
import lombok.RequiredArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/hello")
@RequiredArgsConstructor
public class HelloController {

    private final IPlayerRepository playerRepository;
    private final IQuizRepository quizRepository;
    private final IPlayerMapper playerMapper;
    private final IQuizMapper quizMapper;

    @GetMapping
    public String helloBack() {
        return "Hello";
    }

    @PostMapping
    public ResponseEntity<PlayerDto> getPlayer(@RequestBody EnterPlaygroundRequest payload) {
        var quiz = quizRepository.findById(new ObjectId(payload.getQuizId()))
            .orElseThrow(() -> new ItemNotFoundException("Cannot quiz id %s".formatted(payload.getQuizId())));
        String playerId = makePlayerId(payload.getQuizId(), payload.getUsername());
        Player player = playerRepository.findById(playerId)
            .orElseGet(() -> playerRepository.save(Player.builder()
                                .id(playerId)
                                .username(payload.getUsername())
                                .score(0L)
                                .riddlePassed(0)
                                .build()));
        var playerDto = playerMapper.entityToExtendedDto(player);
        playerDto.setQuiz(quizMapper.entityToDto(quiz));
        return ResponseEntity.ok(playerDto);
    }

    private String makePlayerId(String quizId, String username) {
        return "%s__%s".formatted(quizId, username);
    }

}
