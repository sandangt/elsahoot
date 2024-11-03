package elsahoot.console.dto.core;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

import java.util.List;

@Data
@Builder
@AllArgsConstructor
public class RiddleDto {

    private String id;
    private String title;
    private String content;
    private List<String> answerList;
    private Integer answer;

    private Long createdAt;
    private Long modifiedAt;

}
