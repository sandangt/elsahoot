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

import java.util.List;

import static elsahoot.console.constant.TableName.RIDDLE;

@Document(collection = RIDDLE)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Riddle {

    @Id
    private ObjectId id;
    private String title;
    private String content;
    private List<String> answerList;
    private Integer answer;

    @CreatedDate
    private Long createdAt;
    @LastModifiedDate
    private Long modifiedAt;

}
