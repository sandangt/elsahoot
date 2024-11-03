package elsahoot.console.dto.extended;

import elsahoot.console.dto.core.QuizDto;
import elsahoot.console.dto.core.RiddleDto;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.SuperBuilder;

import java.util.List;

@Data
@SuperBuilder
@EqualsAndHashCode(callSuper = true)
public class QuizExtendedDto extends QuizDto {
    private List<RiddleDto> riddles;
}
