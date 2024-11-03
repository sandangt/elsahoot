package elsahoot.console.dto.core;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.experimental.SuperBuilder;

@Data
@SuperBuilder
@AllArgsConstructor
public class PlayerDto {

    private String id;
    private String username;
    private Long score;
    private Integer riddlePassed;

    private Long createdAt;
    private Long modifiedAt;

}
