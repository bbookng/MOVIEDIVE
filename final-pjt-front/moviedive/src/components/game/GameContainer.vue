<template>
  <div id="game-container">
    <div v-if="inLobby" id="lobby-container" class="row">
      <div class="col-2">
        <div id="connected-users-list">
          <div>My profile</div>
          <div v-for="user in connectedUsers" :key="user.socketId">
            <ConnectedUser :user="user" />
          </div>
        </div>
      </div>
      <div class="col-10">
        <div id="room-creation-form">
          <input v-model="roomName" type="text" />
          <div class="dropdown">
            <button
              class="dropdown-toggle"
              type="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              게임 유형
            </button>
            <ul class="dropdown-menu">
              <li value="1">인물 퀴즈</li>
              <li value="2">OX퀴즈</li>
            </ul>
          </div>
          <button @click="createRoom(roomName, roomType)">생성</button>
        </div>
        <div id="room-list" class="container">
          <div class="row">
            <div
              class="room-list-item col-6 px-0 py-1"
              @click="joinRoom(room.roomId)"
              v-for="room in rooms"
              :key="room.roomId"
            >
              <PlayRoom :room="room" />
            </div>
          </div>
        </div>
        <div id="chatting-room">ChattingRoom</div>
      </div>
    </div>
    <div v-if="inRoom" id="room-container">룸입니다.</div>
  </div>
</template>

<script>
import io from "socket.io-client";
import ConnectedUser from "./gamecontainer/ConnectedUser.vue";
import PlayRoom from "./gamecontainer/PlayRoom.vue";
import { mapGetters } from "vuex";

export default {
  name: "GameContainer",
  components: {
    ConnectedUser,
    PlayRoom,
  },
  data() {
    return {
      connectedUsers: [],
      rooms: [],
      chattings: [],
      SERVER: "http://localhost:5002",
      socket: null,
      room: {},
      roomName: "",
      roomType: 0,
      userLocation: "lobby",
      isReady: false,
    };
  },
  computed: {
    ...mapGetters(["currentUser"]),
    inLobby() {
      return this.userLocation == "lobby";
    },
    inRoom() {
      return this.userLocation == "room";
    },
  },
  methods: {
    connectWithSocketIOServer() {
      this.socket = io(this.SERVER);

      this.socket.on("connect", () => {
        console.log("successfully connected with socket io server");
        console.log(this.socket.id);
      });

      this.socket.on("update-lobby", ({ connectedUsers, rooms }) => {
        this.connectedUsers = connectedUsers;
        this.rooms = rooms;
      });

      this.socket.on("enter-room", ({ room }) => {
        this.userLocation = "Room";
        this.room = room;
      });
    },
    joinLobby(nickname, profile_img) {
      const data = {
        nickname,
        profile_img,
      };
      this.socket.emit("join-lobby", data);
    },
    createRoom(roomName, roomType) {
      const data = {
        roomName,
        roomType,
      };
      this.socket.emit("create-room", data);
    },
    joinRoom(roomId) {
      console.log("start-join room");
      const data = {
        roomId,
      };
      this.socket.emit("join-room", data);
    },
    leaveLobby() {
      this.socket.emit("leave-lobby");
    },
  },
  created() {
    this.connectWithSocketIOServer();
    this.joinLobby(this.currentUser.nickname, this.currentUser.profile_img);
  },
  destroyed() {
    console.log("왜?");
    this.leaveLobby();
  },
  // beforeDestroyed() {
  //
  // },
};
</script>

<style>
#game-container {
  height: 70vh;
  width: 120vh;
  padding: 1%;
  border: 4px black solid;
}

#lobby-container {
  height: 100%;
}
/* =================== User List ====================== */
#connected-users-list {
  border: solid 1px black;
  height: 100%;
}

/* ================== Room Creation Form ================ */
#room-creation-form {
  border: solid 1px black;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 10%;
}

/* ==================== Room List ======================= */
#room-list {
  border: solid 1px black;
  height: 60%;
}

.room-list-item {
  cursor: pointer;
}
/* =================== Chatting Room ===================== */
#chatting-room {
  border: solid 1px black;
  height: 30%;
}
</style>