<template>
  <div>
    <div id="profile-top">
        {{ profileImg }}
        <div id="profile-image">
          <img :src=profileImg alt="프로필 이미지 넣자">
        </div>
        <div id="profile-top-right">
          <div>
            {{ user.nickname }}
            <button v-if="isNotMe" @click="follow">팔로우</button>
          </div>
          <div>
            리뷰 {{ user.reviews_cnt }} |
            팔로워 {{ user.followers_cnt }} |
            팔로잉 {{ user.followings_cnt }} |
          </div>
          <div>
            {{ user.message }}
          </div>
        </div>
        <div>
          {{ collection_highlight }}
        </div>
      </div>
      <div>
        <button @click="getUserReviews">리뷰</button>
        <button @click="getUserCollections">컬렉션</button>
        <button @click="getUserLikes">좋아요</button>
      </div>
      <div>
        <UserReview :user="user" v-if="select_component == 1"/>
        <UserCollection :user="user" v-if="select_component == 2"/>
        <UserLikesMovies :user="user" v-if="select_component == 3"/>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import UserCollection from '@/components/profile/UserCollection.vue'
import UserLikesMovies from '@/components/profile/UserLikesMovies.vue'
import UserReview from '@/components/profile/UserReview.vue';

export default {
  name: 'MyPage',
  components: {
    UserCollection,
    UserLikesMovies,
    UserReview,
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
      const API_URL = 'http://127.0.0.1:8000/api' 
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
      const API_URL = 'http://127.0.0.1:8000/api'
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