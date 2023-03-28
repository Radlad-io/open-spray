// import mqtt from "mqtt";

export default class Network {
  constructor(connectionUrl, username, token, topicName) {
    this.clean = true;
    this.connectionTimeout = 4000;
    this.connectionUrl = connectionUrl;
    this.username = username;
    this.password = token;
    this.topicName = topicName;

    this.options = {
      clean: this.clean,
      connectTimeout: this.connectionTimeout,
      username: this.username,
      password: this.password,
    };
    this.client = mqtt.connect(this.connectionUrl, this.options);

    this.init();
  }

  init() {
    this.client.on("connect", (connection) => {
      console.log("Connected", connection);
      this.client.subscribe(this.topicName, (err, granted) => {
        if (err) {
          console.log(err);
        }
        console.log(granted, "granted");
      });
    });

    this.client.on("reconnect", (error) => {
      console.log("reconnecting:", error);
    });

    this.client.on("error", (error) => {
      console.log("Connection failed:", error);
    });

    this.client.on("message", (topic, message) => {
      console.log("receive message：", topic, message.toString());
    });
  }
}
