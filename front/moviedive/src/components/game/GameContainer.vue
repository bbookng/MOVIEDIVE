<template>
  <div id="game-container" class="row">
    <div class="col-2">
      <ConnectedUserList :connectedUsers="connectedUsers" />
    </div>
    <div class="col-10">
      <RoomCreationForm />
      <RoomList />
      <ChattingRoom />
    </div>
  </div>
</template>

<script>
import RoomList from "./gamecontainer/RoomList.vue";
import ConnectedUserList from "./gamecontainer/ConnectedUserList.vue";
import RoomCreationForm from "./gamecontainer/RoomCreationForm.vue";
import ChattingRoom from "./gamecontainer/ChattingRoom.vue";
import io from "socket.io-client";
import { mapGetters } from "vuex";

export default {
  name: "GameContainer",
  components: {
    RoomList,
    ConnectedUserList,
    ChattingRoom,
    RoomCreationForm,
  },
  data() {
    return {
      connectedUsers: [],
      rooms: [],
      chattings: [],
      inRoom: false,
      SERVER: "http://localhost:5002",
      socket: null,
    };
  },
  computed: {
    ...mapGetters(["currentUser"]),
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
    },
    joinLobby(nickname, profile_img) {
      const data = {
        nickname,
        profile_img,
      };
      this.socket.emit("join-lobby", data);
    },
  },
  created() {
    this.connectWithSocketIOServer();
  },
};
</script>

<style>
#game-container {
  height: 70vh;
  width: 120vh;
  padding: 1%;
  border: 4px black solid;
}
</style>