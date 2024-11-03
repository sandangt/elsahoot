package elsahoot.console.viewmodel.request;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class EnterPlaygroundRequest {
    private String quizId;
    private String username;
}
