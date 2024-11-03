package elsahoot.console.mapper;

import elsahoot.console.dto.core.PlayerDto;
import elsahoot.console.dto.extended.PlayerExtendedDto;
import elsahoot.console.model.Player;
import org.mapstruct.BeanMapping;
import org.mapstruct.IterableMapping;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.Named;
import org.mapstruct.NullValueCheckStrategy;

import java.util.List;

@Mapper(componentModel = "spring")
public interface IPlayerMapper {

    @Named("entityToDto")
    PlayerDto entityToDto(Player player);

    @Named("entityToDtoIter")
    @IterableMapping(qualifiedByName = "entityToDto")
    List<PlayerDto> entityToDto(List<Player> players);

    @Named("entityToExtendedDto")
    PlayerExtendedDto entityToExtendedDto(Player player);

    @Named("entityToExtendedDtoIter")
    @IterableMapping(qualifiedByName = "entityToExtendedDto")
    List<PlayerExtendedDto> entityToExtendedDto(List<Player> players);

    @Named("dtoToEntity")
    @Mapping(target = "quizId", ignore = true)
    @BeanMapping(nullValueCheckStrategy = NullValueCheckStrategy.ALWAYS)
    Player dtoToEntity(PlayerDto player);

    @Named("dtoToEntityIter")
    @IterableMapping(qualifiedByName = "dtoToEntity")
    List<Player> dtoToEntity(List<PlayerDto> players);

}
