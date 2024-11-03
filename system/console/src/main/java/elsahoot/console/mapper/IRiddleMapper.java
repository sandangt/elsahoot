package elsahoot.console.mapper;

import elsahoot.console.dto.core.RiddleDto;
import elsahoot.console.model.Riddle;
import org.mapstruct.IterableMapping;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.Named;

import java.util.List;

@Mapper(componentModel = "spring")
public interface IRiddleMapper extends IBaseMapper {

    @Named("entityToDto")
    @Mapping(target = "id", source = "id", qualifiedByName = "objectIdToString")
    RiddleDto entityToDto(Riddle riddle);

    @Named("entityToDtoIter")
    @IterableMapping(qualifiedByName = "entityToDto")
    List<RiddleDto> entityToDto(List<Riddle> riddles);

    @Named("dtoToEntity")
    @Mapping(target = "id", source = "id", qualifiedByName = "stringToObjectId")
    Riddle dtoToEntity(RiddleDto riddle);

    @Named("dtoToEntityIter")
    @IterableMapping(qualifiedByName = "dtoToEntity")
    List<Riddle> dtoToEntity(List<RiddleDto> riddles);

}
