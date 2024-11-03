package elsahoot.console.dto.extended;

import elsahoot.console.dto.core.PlayerDto;
import elsahoot.console.dto.core.QuizDto;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
@EqualsAndHashCode(callSuper = true)
public class PlayerExtendedDto extends PlayerDto {
    private QuizDto quiz;
}
