package elsahoot.console.mapper;

import elsahoot.console.dto.core.QuizDto;
import elsahoot.console.dto.extended.QuizExtendedDto;
import elsahoot.console.model.Quiz;
import org.mapstruct.IterableMapping;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.Named;

import java.util.List;

@Mapper(componentModel = "spring")
public interface IQuizMapper extends IBaseMapper {

    @Named("entityToDto")
    @Mapping(target = "id", source = "id", qualifiedByName = "objectIdToString")
    QuizDto entityToDto(Quiz quiz);

    @Named("entityToDtoIter")
    @IterableMapping(qualifiedByName = "entityToDto")
    List<QuizDto> entityToDto(List<Quiz> quizzes);

    @Named("entityToExtendedDto")
    @Mapping(target = "id", source = "id", qualifiedByName = "objectIdToString")
    QuizExtendedDto entityToExtendedDto(Quiz quiz);

    @Named("entityToExtendedDtoIter")
    @IterableMapping(qualifiedByName = "entityToExtendedDto")
    List<QuizExtendedDto> entityToExtendedDto(List<Quiz> quizzes);

    @Named("dtoToEntity")
    @Mapping(target = "id", source = "id", qualifiedByName = "stringToObjectId")
    Quiz dtoToEntity(QuizDto quiz);

    @Named("dtoToEntityIter")
    @IterableMapping(qualifiedByName = "dtoToEntity")
    List<Quiz> dtoToEntity(List<QuizDto> quizses);
}
