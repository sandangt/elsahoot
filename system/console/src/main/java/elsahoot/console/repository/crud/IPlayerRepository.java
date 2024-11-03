package elsahoot.console.repository.crud;

import elsahoot.console.model.Player;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface IPlayerRepository extends MongoRepository<Player, String> {}
