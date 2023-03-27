const express = require("express");
const path = require("path");
const app = express();

const PORT = process.env | 5000;

app.get("/", (req, res) => {
  res.json({
    msg: "You hit the V1 API",
    from: "Server",
  });
  console.log(req);
});

app.listen(PORT, () => {
  console.log(``);
  console.log(`  > Local REST: http://localhost:${PORT}/api/v1`);
  // console.log(`  > Local Socket: ws://localhost:${WS_PORT}`);
});
