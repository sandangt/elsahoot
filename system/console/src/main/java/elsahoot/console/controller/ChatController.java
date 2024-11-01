package elsahoot.console.controller;

import elsahoot.console.dto.ChatMessage;
import org.springframework.messaging.handler.annotation.Header;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.messaging.simp.annotation.SendToUser;
import org.springframework.stereotype.Controller;

@Controller
public class ChatController {

    @MessageMapping("/broadcast")
    @SendTo("/topic/reply")
    public ChatMessage sendMessage(ChatMessage chatMessage) {
        return chatMessage;
    }

    @MessageMapping("/user-message")
    @SendToUser("/queue/reply")
    public String sendBackToUser(@Payload String message, @Header("simpSessionId") String sessionId) {
        return "Only you have received this message: " + message;
    }

}
