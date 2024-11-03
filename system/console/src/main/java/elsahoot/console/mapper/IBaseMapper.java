package elsahoot.console.mapper;

import org.bson.types.ObjectId;
import org.mapstruct.Named;

public interface IBaseMapper {
    @Named("objectIdToString")
    default String objectIdToString(ObjectId id) {
        return String.valueOf(id);
    }

    @Named("stringToObjectId")
    default ObjectId StringToObjectId(String id) {
        try {
            return new ObjectId(id);
        } catch (Exception ignore) {
            return null;
        }
    }

}
