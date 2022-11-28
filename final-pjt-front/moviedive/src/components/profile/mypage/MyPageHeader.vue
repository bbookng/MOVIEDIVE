<template>
  <div v-if="user" id="my-page-header" class="container">
    <div class="row">
      <div class="col-4 d-flex justify-content-end">
        <div id="profile-img-box">
          <img
            id="profile-img"
            style="padding:0;"
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
            <div id="user-nickname">{{ user.nickname }}</div>
            <button @click="follow" v-if="currentUser.username != user.username" id="follow-button" class="mx-3">팔로우</button>
          </div>
          <div class="my-2 d-flex justify-content-between">
            <div>
              리뷰 {{ user.reviews_cnt }} 
            </div>
            <div class="mx-2">
              팔로워 {{ user.followers_cnt }} 
            </div>
            <div>
              팔로우 {{ user.followings_cnt }} 
            </div>
          </div>
          <div class="status none" v-if="!user.message">상태메시지가 없습니다.</div>
          <div class="status">{{ user.message }}</div>
        </div>
      </div>
    </div>
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
      const API_URL = "https://moviedive.co.kr/api";
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
      const API_URL = "https://moviedive.co.kr/api";
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

#user-nickname {
  font-size: 25px;
  font-weight: bold;
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

.none {
  color: grey;
}
</style>