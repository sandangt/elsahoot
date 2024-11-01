import { Container } from '@mui/material'
import { useEffect, useState } from 'react'

export const HomePage = () => {
  const [playerId, setPlayerId] = useState(Math.floor(new Date().getTime() / 1000))
  const [chatHistory, setChatHistory] = useState([]);
  const [isOnline, setIsOnline] = useState(false);
  const [textValue, setTextValue] = useState("");
  const [websckt, setWebsckt] = useState();

  const [message, setMessage] = useState<string[]>([]);
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const url = "ws://localhost:8000/test/ws/" + playerId;
    const ws = new WebSocket(url);

    ws.onopen = () => {
      ws.send("Connect");
    };

    // recieve message every start page
    ws.onmessage = (e) => {
      const message = JSON.parse(e.data);
      setMessages([...messages, message]);
    };

    setWebsckt(ws);
    //clean up function when we close page
    return () => ws.close();
  }, [message,messages]);

  const sendMessage = () => {
    websckt.send(message);
    // recieve message every send message
    websckt.onmessage = (e) => {
      const message = JSON.parse(e.data);
      setMessages([...messages, message]);
    };
    setMessage([]);
  };
  return (
    <Container>
      <h1>Chat</h1>
      <h2>Your player id: {playerId} </h2>
      <div className="chat-container">
        <div className="chat">
          {messages.map((value, index) => {
            if (value.playerId === playerId) {
              return (
                <div key={index} className="my-message-container">
                  <div className="my-message">
                    <p className="client">client id : {playerId}</p>
                    <p className="message">{value.message}</p>
                  </div>
                </div>
              );
            } else {
              return (
                <div key={index} className="another-message-container">
                  <div className="another-message">
                    <p className="client">client id : {playerId}</p>
                    <p className="message">{value.message}</p>
                  </div>
                </div>
              );
            }
          })}
        </div>
        <div className="input-chat-container">
          <input
            className="input-chat"
            type="text"
            placeholder="Chat message ..."
            onChange={(e) => setMessage(e.target.value)}
            value={message}
          ></input>
          <button className="submit-chat" onClick={sendMessage}>
            Send
          </button>
        </div>
      </div>
    </Container>
  );
}
