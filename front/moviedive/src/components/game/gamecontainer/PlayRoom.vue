<template>
  <div class="room-container d-flex">
    <div class="room-type">
      <img
        v-if="room.roomType"
        src="https://lh3.googleusercontent.com/I8LhmbcHdnRpF5kTz0jRNsW4YXPNfJ-mrSGl1c2e8PjsluWlUXjX6EaiMfvT-Sz2nLet=w800-h500-rw"
        alt=""
      />
      <img
        v-if="!room.roomType"
        src="https://png.pngtree.com/element_our/20190602/ourlarge/pngtree-gray-movie-supplies-illustration-image_1410373.jpg"
        alt=""
      />
    </div>

    <div class="room-info">
      <div class="room-container-top d-flex align-items-center">
        <p class="room-id">{{ preprocessed_roomId }}</p>
        <p class="room-name">{{ room.roomName }}</p>
      </div>
      <div
        class="
          room-container-bottom
          d-flex
          justify-content-between
          align-items-center
        "
      >
        <p class="room-status">{{ room.status }}</p>
        <p class="room-people">{{ room.connectedUsers.length }}/6</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PlayRoom",
  props: {
    room: Object,
  },
  computed: {
    preprocessed_roomId() {
      let num = this.room.roomId.toString();
      while (num.length < 3) num = "0" + num;

      return num;
    },
  },
};
</script>

<style>
.room-container {
  border: black 1px solid;
  border-radius: 10px;
  height: 100px;
  margin: 5px;
  margin-left: 10px;
  margin-right: 10px;
  padding: 10px;
}
.room-type {
  height: 80px;
  width: 80px;
  border-radius: 10px;
  overflow: hidden;
}
.room-type img {
  height: 80px;
  width: 80px;
}
.room-info {
  width: 100%;
  padding-left: 15px;
}
.room-container-top {
  border: black 1px solid;
  border-radius: 10px;
  background-color: snow;
  height: 40px;
  padding: 5px;
}

.room-id {
  border: black 1px solid;
  border-radius: 8px;
  margin: 0;
  width: 45px;
}
.room-name {
  margin: 0;
  margin-left: 20px;
}

.room-container-bottom {
  margin-top: 2px;
  height: 40px;
  padding: 5px;
}
.room-status {
  padding-left: 3px;
  font-size: 22px;
  font-weight: bold;
  margin: 0;
}
.room-people {
  padding-top: 4px;
  margin: 0;
}
</style>