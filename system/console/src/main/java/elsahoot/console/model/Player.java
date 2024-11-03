package elsahoot.console.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.domain.Persistable;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.MongoId;

import static elsahoot.console.constant.TableName.PLAYER;

@Document(collection = PLAYER)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Player implements Persistable<String> {

    @MongoId
    private String id;
    private String username;
    private Long score;
    private Integer riddlePassed;
    private ObjectId quizId;

    @CreatedDate
    private Long createdAt;
    @LastModifiedDate
    private Long modifiedAt;

    @Override
    public boolean isNew() {
        return createdAt == null;
    }
}
