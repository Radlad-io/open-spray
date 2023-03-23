const express = require("express");
const path = require("path");
const app = express();

// Importing the required modules
const WebSocketServer = require("ws");

const PORT = process.env | 5000;
const WS_PORT = 5001;

// Creating a new websocket server
const wss = new WebSocketServer.Server({ port: WS_PORT });

// app.use("/", express.static(path.join(__dirname, "public")));
// app.get("/*", (_req, res) => {
//   res.sendFile(path.join(__dirname, "public", "index.html"));
// });

app.get("/", (req, res) => {
  res.json({
    msg: "You hit the V1 API",
    from: "Server",
  });
  console.log(req);
});

wss.on("connection", (ws) => {
  console.log("new client connected");

  // sending message to client
  ws.send("Welcome, you are connected!");

  //on message from client
  ws.on("message", (data) => {
    console.log(`Client has sent us: ${data}`);
  });

  // handling what to do when clients disconnects from server
  ws.on("close", () => {
    console.log("the client has disconnected");
  });
  // handling client connection error
  ws.onerror = function () {
    console.log("Some Error occurred");
  };
});

app.listen(PORT, () => {
  console.log(``);
  console.log(`  > Local REST: http://localhost:${PORT}/api/v1`);
  console.log(`  > Local Socket: ws://localhost:${WS_PORT}`);
});
