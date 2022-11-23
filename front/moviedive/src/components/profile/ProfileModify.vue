<template>
  <div>
    <div id="profile-img-box">
      <img
        id="profile-img"
        :src=profileImg
        alt="프로필 이미지"
      />
    </div>
    <div>
      <input
        @change="onInputImage"
        type="file"
        ref="profileImage"
        accept="image/*"
        id="file"
      />
      <button type="button" @click="onClickFormButton">upload!</button>
    </div>
    <div>
      <div v-if="!flag">
        <p>{{ nickname }}</p>
        <p>{{ message }}</p>
        <button @click="editButton">프로필 수정</button>
      </div>
      <div v-if="flag">
        <form @submit.prevent="updateProfile">
          <label for="usernickname">닉네임: </label>
          <input
            type="text"
            id="usernickname"
            v-model="nickname"
          />
          <label for="usermessage">상태메세지: </label>
          <input
            type="text"
            id="usermessage"
            v-model="message"
          />
          <input type="submit" value="수정" />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000/api";

export default {
  name: "ProfileModify",
  data() {
    return {
      image: "",
      nickname: null,
      message: null,
      flag: false,
    };
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser;
    },
    profileImg() {
      return this.currentUser.profile_img;
    },
  },
  methods: {
    onInputImage() {
      this.image = this.$refs.profileImage.files;
      console.log(this.image);
    },
    onClickFormButton() {
      const formdata = new FormData();
      formdata.append("profile_img", this.image[0]);
      console.log("formdata", formdata);

      axios({
        method: "put",
        url: "/api/accounts/profileimg/",
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": true,
          "Access-Control-Allow-Headers": "*",
          "Content-Type": "multipart/form-data",
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: formdata,
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    setProfileForm() {
      axios({
        method: "get",
        url: `${API_URL}/accounts/profile/${this.currentUser.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.nickname = res.data.nickname
          this.message = res.data.message
          console.log(res.data);
        })
    },
    updateProfile() {
      const nickname = this.nickname;
      const message = this.message;

      axios({
        method: "put",
        url: `${API_URL}/accounts/profile/${this.currentUser.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          nickname,
          message,
        },
      })
        .then((res) => {
          this.setProfileForm()
          this.flag = false,
          this.$store.commit('GET_ACCOUNT_MODIFY', 1)
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    editButton() {
      this.flag = true
    }
  },
  created() {
    this.setProfileForm()
  }
};
</script>

<style>
</style>