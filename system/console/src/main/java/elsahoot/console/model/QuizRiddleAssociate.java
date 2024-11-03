package elsahoot.console.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import static elsahoot.console.constant.TableName.QUIZ_RIDDLE;

@Document(collection = QUIZ_RIDDLE)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class QuizRiddleAssociate {

    @Id
    private ObjectId id;
    private ObjectId quizId;
    private ObjectId riddleId;

}
