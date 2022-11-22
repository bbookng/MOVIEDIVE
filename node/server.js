const express = require("express");
const http = require("http");
const cors = require("cors");

const PORT = 5002;
const app = express();
const server = http.createServer(app);

app.use(cors());

const io = require("socket.io")(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"],
  },
});

connectedUsers = [];
rooms = [];

io.on("connection", (socket) => {
  console.log(`user connected ${socket.id}`);

  socket.on("join-lobby", (data) => {
    console.log(`${socket.id}가 로비에 들어왔습니다.`)
    joinLobbyHandler(data, socket);
  });
  socket.on("create-room", (data) => {
    console.log(`${socket.id}가 방을 만들었습니다.`)
    createRoomHandler(data, socket);
  });
})

// ===================== Handler =======================
const joinLobbyHandler = (data, socket) => {
  const { profile_img, nickname } = data

  newUser = {
    profile_img,
    nickname,
    socketId: socket.id
  }

  connectedUsers = [...connectedUsers, newUser]

  data = {
    rooms,
    connectedUsers,
  }

  io.emit("update-lobby", data)
}

const createRoomHandler = (data, socket) => {

}

server.listen(5002, () => {
  console.log("server start on 5002");
})