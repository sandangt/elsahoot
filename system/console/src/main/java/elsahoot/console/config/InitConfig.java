package elsahoot.console.config;

import elsahoot.console.service.FakeService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@Slf4j
@RequiredArgsConstructor
public class InitConfig {

    private final FakeService fakeService;

    @Bean
    CommandLineRunner initData() {
        fakeService.seedRiddle(10000);
        fakeService.seedQuiz(100);
        return args -> log.info("Init data done");
    }

}
