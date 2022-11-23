<template>
  <div v-if="user">
    <MyPageHeader :profileImg="profileImg" :user="user" />
    <div>
      <button @click="getUserReviews">리뷰</button>
      <button @click="getUserCollections">컬렉션</button>
      <button @click="getUserLikes">좋아요</button>
    </div>
    <div>
      <UserReview :user="user" v-if="select_component == 1" />
      <UserCollection :user="user" v-if="select_component == 2" />
      <UserLikesMovies :user="user" v-if="select_component == 3" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MyPageHeader from "./mypage/MyPageHeader.vue";
import UserCollection from "@/components/profile/UserCollection.vue";
import UserLikesMovies from "@/components/profile/UserLikesMovies.vue";
import UserReview from "@/components/profile/UserReview.vue";

export default {
  name: "MyPage",
  components: {
    UserCollection,
    UserLikesMovies,
    UserReview,
    MyPageHeader,
  },
  data() {
    return {
      collection_highlight: [],
      select_component: 1,
      user: null,
      isNotMe: true,
    };
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser;
    },
    profileImg() {
      return this.currentUser.profile_img;
    },
    mypage() {
      return this.$store.state.mypage;
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
        .then(() => {
          this.checkUser();
        });
    },
    getUserReviews() {
      this.select_component = 1;
    },
    getUserCollections() {
      this.select_component = 2;
    },
    getUserLikes() {
      this.select_component = 3;
    },
    checkUser() {
      if (this.currentUser.username == this.user.username) {
        return (this.isNotMe = false);
      } else {
        return (this.isNotMe = true);
      }
    },
  },
  created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>

<style scoped>
button {
  border: none;
  border-top: black 1px solid;
  background-color: transparent;
  width: 100px;
  font-size: large;
  margin: 20px;
}

</style>