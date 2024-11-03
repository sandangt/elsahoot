package elsahoot.console.dto.core;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
@AllArgsConstructor
public class QuizDto {

    private String id;
    private String topic;
    private Long totalScore;

    private Long createdAt;
    private Long modifiedAt;

}
