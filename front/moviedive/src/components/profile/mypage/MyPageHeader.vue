<template>
  <div v-if="user" id="my-page-header" class="container">
    <div class="row">
      <div class="col-4 d-flex justify-content-end">
        <div id="profile-img-box">
          <img
            id="profile-img"
            :src=profileImg
            alt="프로필 이미지"
          />
        </div>
      </div>
      <div class="col-8 d-flex align-items-end">
        <div
          id="profile-informations"
          class="d-flex flex-column justify-content-end align-items-start"
        >
          <div class="d-flex align-items-center">
            <div>{{ user.nickname }}</div>
            <button @click="follow" v-if="currentUser.username != user.username" id="follow-button" class="mx-3">팔로우</button>
          </div>
          <div class="my-2 row">
            <div class="col">
              리뷰 {{ user.reviews_cnt }}
            </div>
            <div class="col">
              팔로워 {{ user.followers_cnt }}
            </div>
            <div class="col">
              팔로우 {{ user.followings_cnt }}
            </div>
          </div>
          <div class="status">{{ user.message }}</div>
        </div>
      </div>
    </div>
    <div id="highlights" class="row">하이라이트 컬렉션 들어갈 자리</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "MyPageHeader",
  data() {
    return {
      user: null,
      highlight: []
    }
  },
  props: {
    profileImg: String,
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser
    },
  },
  methods: {
    fetchProfile(username) {
      const API_URL = "http://127.0.0.1:8000/api";
      axios({
        method: "get",
        url: `${API_URL}/accounts/profile/${username.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.user = res.data;
        })
    },
    follow() {
      const API_URL = "http://127.0.0.1:8000/api";
      axios({
        url: `${API_URL}/accounts/profile/${this.user.pk}/follow/`,
        method: "post",
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then(() => {
        console.log('팔로우 성공!')
        this.fetchProfile(this.user)
      })
      .catch(() => {
        console.log('팔로우 실패!')
      })
    },
  },
  created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>

<style>
#my-page-header {
  height: 350px;
}
#profile-img {
  margin-top: 8vh;
  border-radius: 50%;
  border: white 3px solid;
  height: 170px;
  width: 170px;
}
#follow-button {
  background-color: white;
  border: black 1px solid;
  border-radius: 4px;
}
#profile-informations {
  padding-bottom: 40px;
  padding-left: 15px;
}
#highlights {
  border: 1px black solid;
  margin-top: 20px;
  padding-left: 60px;
}
</style>