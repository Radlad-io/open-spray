const express = require("express");
const path = require("path");
const app = express();
const ws = require("ws");

const router = express.Router();
const imageRegex = /\/.+\.(svg|png|jpg|png|jpeg)$/; // You can add other image formats
const videoRegex = /\/.+\.(mp4|ogv)$/;

app.use("/", express.static(path.join(__dirname, "public")));
app.get("/api/v1", (req, res) => {
  res.json({
    project: "React and Express Boilerplate",
    from: "Vanaldito",
  });
});
app.get("/*", (_req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});
router.get(imageRegex, (req, res) => {
  const filePath = req.path;
  res.redirect(303, `http://localhost:3000/src${filePath}`);
});
router.get(videoRegex, (req, res) => {
  const filePath = req.path;
  res.redirect(303, `http://localhost:3000/src${filePath}`);
});
const { PORT = 5000 } = process.env;
app.listen(PORT, () => {
  console.log();
  console.log(`  App running in port ${PORT}`);
  console.log();
  console.log(`  > Local: \x1b[36mhttp://localhost:\x1b[1m${PORT}/\x1b[0m`);
});

// Set up a headless websocket server that prints any
// events that come in.
const wsServer = new ws.Server({ noServer: true });
wsServer.on("connection", (socket) => {
  socket.on("message", (message) => console.log(message));
});

// `server` is a vanilla Node.js HTTP server, so use
// the same ws upgrade process described here:
// https://www.npmjs.com/package/ws#multiple-servers-sharing-a-single-https-server
const server = app.listen(3000);
server.on("upgrade", (request, socket, head) => {
  wsServer.handleUpgrade(request, socket, head, (socket) => {
    wsServer.emit("connection", socket, request);
  });
});
