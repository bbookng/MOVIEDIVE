<template>
  <div>
    <div>
      <img src=profileImg alt="프로필 이미지">
      <input @change='onInputImage' type="file" ref="profileImage" accept="image/*" id="file" />
      <button type="button" @click="onClickFormButton">upload!</button>
    </div>
    <div>
      <div>
        {{ currentUser.username }}
        {{ currentUser.email }}
        
      </div>
      <div>
        <p>{{ currentUser.nickname }}</p>
        <p>{{ currentUser.message }}</p>
        <button @click="setProfileForm">프로필 수정</button>
      </div>
      <div>
        <form @submit.prevent="updateProfile">
          <label for="usernickname">닉네임: </label>
          <input type="text" id="usernickname" v-model="nickname" value="usernickname">
          <label for="usermessage">상태메세지: </label>
          <input type="text" id="usermessage" v-model="message" value="usermessage">
          <input type="submit" value="수정">
        </form> 
      </div>
    </div>

  </div>
</template>

<script>
import axios  from 'axios'

const API_URL = 'http://127.0.0.1:8000/api'

export default {
  name: 'ProfileModify',
  data() {
    return {
      image: '',
      nickname: null,
      message: null,
    } 
  },
  computed: {
    currentUser () {
      return this.$store.getters.currentUser
    },
    profileImg() {
      return this.currentUser.profile_img
    },
    usernickname() {
      return this.currentUser.nickname
    },
    usermessage() {
      return this.currentUser.message
    }
  },
  methods: {
    onInputImage() {
      this.image = this.$refs.profileImage.files
      console.log(this.image)
    },
    onClickFormButton() {
      const formdata = new FormData()
      formdata.append('profile_img', this.image[0])

      axios({
        method:'put',
        url: `${API_URL}/api/accounts/profileimg/`,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Credentials': true,
          'Access-Control-Allow-Headers': '*',
          'Content-Type': 'multipart/form-data',
          Authorization: `Token ${this.$store.state.token}`
        },
        data: formdata
      })
      .then((res) => { 
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    setProfileForm() {

    },
    updateProfile() {
      const nickname = this.nickname
      const message = this.message

      axios({
        method: 'put',
        url: `${API_URL}/accounts/profile/update/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          nickname,
          message
        }
      })
      .then((res) => {
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>