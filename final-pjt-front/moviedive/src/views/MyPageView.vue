<template>
  <div>
    <MyPage v-if="this.mypage == 1"/>
    <ProfileModify v-if="this.mypage == 2"/>
    <AccountModify v-if="this.mypage == 3"/>
  </div>
  
</template>

<script>
import axios from 'axios'
import ProfileModify from '@/components/profile/ProfileModify.vue';
import AccountModify from '@/components/profile/AccountModify.vue';
import MyPage from '@/components/profile/MyPage.vue'

export default {
  name: 'MyPageView',
  components: {
    ProfileModify,
    AccountModify,
    MyPage
  },
  data() {
    return {
      collection_highlight: [],
      select_component : 1,
      user: null,
      isNotMe: true,
    }
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser
    },
    profileImg() {
      return this.currentUser.profile_img
    },
    mypage() {
      return this.$store.state.mypage
    }
  },
  methods: {
    fetchProfile(username) {
      const API_URL = 'https://moviedive.co.kr/api' 
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${username.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.user = res.data
      })
      .then(() => {
        this.checkUser()
      })
    },
    getUserReviews() {
      this.select_component = 1
    },
    getUserCollections() {
      this.select_component = 2
    },
    getUserLikes() {
      this.select_component = 3
    },
    follow() {
      const API_URL = 'https://moviedive.co.kr/api'
      console.log(this.user)
      axios({
        url: `${API_URL}/accounts/profile/${this.user.pk}/follow/`,
        method: 'post',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => { 
        this.fetchProfile(this.user)
      })

    },
    checkUser() {
      if (this.currentUser.username == this.user.username) {
        return this.isNotMe = false
      } else {
        return this.isNotMe = true
      }
    }
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  }

}
</script>

<style>

</style>