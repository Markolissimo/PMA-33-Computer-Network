const webSocket = require("ws");

const wss = new webSocket.Server({ port: 8086 });

wss.on("connection", (ws) => {
  console.log("New client connected!");

  ws.on("message", (data) => {
    const d = data.toString("utf8");

    typeof d == "string"
      ? console.log(
          d
            .split("")
            .filter((letter) => letter === letter.toLowerCase())
            .join("")
        )
      : console.log("Type of your message is not a string!");
  });

  ws.on("close", () => {
    console.log("Client has disconnected!");
  });
});
