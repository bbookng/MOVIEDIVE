<template>
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <img :src=mainPosterURL alt="">
        {{ movie_detail.title }} 
        <span><button @click="likeMovie">좋아요</button></span>
        <div>
          {{ movie_detail.vote_average }}
          <span>몇세관람, 러닝타임</span>
        </div>
        <div>
          <button>넷플릭스</button>
          <button>왓챠</button>
          <button>디즈니플러스</button>
        </div>
        <!-- <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> -->
      </div>
      <div class="modal-body">
        <p>{{ movie_detail.overview }}</p>
      </div>
      <div>
        <router-link :to="{ name: 'create_review' }">리뷰 작성하기</router-link>
        <hr>
        <div>
          <p>최근 리뷰</p>
          <div v-for="review in movie_detail.reviews" :key="review.id">
            <span>{{ review.title }}</span> |
            <span>{{ review.created_string}}</span> |
            <span><img src="" alt="유저 프로필 사진"></span>
            <span>{{ review.user.username}}</span>
          </div>
          <router-link :to="{ name: 'community' }">리뷰 더 보기</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api'

export default {
  name: 'MovieDetail',
  data() {
    return {
      movie_detail: null,
      mainPosterURL: null,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    getMovieDetail() {
      axios({
          url: `${API_URL}/movies/${this.movie.pk}/`,
          method: 'get',
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res)=>{
          this.movie_detail = res.data
          this.mainPosterURL = `https://image.tmdb.org/t/p/original/${res.data.backdrop_path}`
        })
    },
    likeMovie() {
      axios({
          url: `${API_URL}/movies/${this.movie_detail.pk}/like/`,
          method: 'post',
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => { 
          this.getMovieDetail()
        })

    }
  },
  created() {
    this.getMovieDetail()
  }

}
</script>

<style scoped>
.modal,
.overlay {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  right: 0;
}

.overlay {
  opacity: 0.5;
  background-color: black;
}

.modal-card {
  position: relative;
  max-width: 80%;
  margin: auto;
  margin-top: 30px;
  padding: 20px;
  background-color: black;
  min-height: 500px;
  z-index: 10;
  opacity: 1;
}

</style>