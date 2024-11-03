package elsahoot.console.repository.crud;

import elsahoot.console.model.QuizRiddleAssociate;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface IQuizRiddleRepository extends MongoRepository<QuizRiddleAssociate, ObjectId> {

    List<QuizRiddleAssociate> findAllByQuizIdIn(List<ObjectId> quizIds);

}
