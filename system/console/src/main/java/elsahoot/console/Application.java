package elsahoot.console;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.mongodb.config.EnableMongoAuditing;
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker;

@SpringBootApplication
@EnableMongoAuditing
@EnableWebSocketMessageBroker
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
