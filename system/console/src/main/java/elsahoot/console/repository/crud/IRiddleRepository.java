package elsahoot.console.repository.crud;

import elsahoot.console.model.Riddle;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface IRiddleRepository extends MongoRepository<Riddle, ObjectId> {
    List<Riddle> findAllByIdIn(List<ObjectId> ids);
}
