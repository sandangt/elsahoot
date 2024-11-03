package elsahoot.console.repository.crud;

import elsahoot.console.model.Quiz;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface IQuizRepository extends MongoRepository<Quiz, ObjectId> {}
