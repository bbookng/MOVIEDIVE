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
        <button>닉네임 변경하기</button>
      </div>
      <div>
        <p>{{ currentUser.message }}</p>
        <button>상태메세지 변경하기</button>
      </div>
    </div>

  </div>
</template>

<script>
import axios  from 'axios'

export default {
  name: 'ProfileModify',
  data() {
    return {
      image: '',
      
    } 
  },
  computed: {
    currentUser () {
      return this.$store.getters.currentUser
    },
    profileImg() {
      return this.currentUser.profile_img
    }
  },
  methods: {
    onInputImage() {
      this.image = this.$refs.profileImage.files
      console.log("this.image")
    },
    onClickFormButton() {
      const formdata = new FormData()
      formdata.append('profile_img', this.image)

      axios({
        method:'put',
        url: `http://127.0.0.1:8000/api/accounts/profileimg/`,
        headers: {
          'Access-Control-Allow-Origin': '*',
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
  }
}
</script>

<style>

</style>