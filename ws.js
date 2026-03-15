const WebSocket = require("ws");

const wss = new WebSocket.Server({ port: 8081 });

wss.on("connection", ws => {
  ws.on("message", msg => {
    wss.clients.forEach(c => {
      if (c.readyState === WebSocket.OPEN) {
        c.send(msg);
      }
    });
  });
});

console.log("WebSocket запущен на 8081");
