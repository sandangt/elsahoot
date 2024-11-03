package elsahoot.console.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.mongodb.core.mapping.Document;

import static elsahoot.console.constant.TableName.QUIZ;

@Document(collection = QUIZ)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Quiz {
    @Id
    private ObjectId id;
    private String topic;
    private Long totalScore;

    @CreatedDate
    private Long createdAt;
    @LastModifiedDate
    private Long modifiedAt;
}
