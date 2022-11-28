<template>
  <div>
    <MainTrailer />
    <div class="hero-vignette vignette-layer">
      <div class="overlay" style="margin: 0 3rem 0 3rem; color: white">'
        <div><h3 class="new-movies-title">최근 핫한 영화들</h3></div>
        <MovieList :movies="new_movies" />'
        <!-- {{ collections }} -->
        <div v-for="collection in collections" :key="collection.pk">
          <div><h3 class="collection-name">{{ collection.title }}</h3></div>
          <MovieList :movies="collection.movies" />
        </div>
        
      </div>
    </div>

    <movie-detail></movie-detail>
  </div>
</template>

<script>
import MovieList from "@/components/movies/MovieList";
import MainTrailer from "@/components/main/MainTrailer.vue";
import MovieDetail from "@/components/movies/MovieDetail.vue";
import { mapActions } from "vuex";
import axios from "axios";

const API_URL = "https://moviedive.co.kr/api";

export default {
  name: "MainView",
  components: {
    MovieList,
    MainTrailer,
    MovieDetail,
  },
  data() {
    return {
      new_movies: null,
    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    collections() {
      return this.$store.state.collections;
    }
  },
  methods: {
    ...mapActions(["fetchMain"]),
    getNewMovies() {
      axios({
        method: "get",
        url: `${API_URL}/movies/new/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then((res) => {
        this.new_movies = res.data;
      });
    },
  },
  created() {
    this.fetchMain();
    this.getNewMovies();
  },
};
</script>

<style scoped>
.overlay {
  z-index: 10;
  position: absolute;
}
.hero-vignette {
  background-color: transparent;
  background-image: linear-gradient(
    180deg,
    hsla(0, 0%, 8%, 0) 0,
    hsla(0, 0%, 8%, 0.15) 15%,
    hsla(0, 0%, 8%, 0.35) 29%,
    hsla(0, 0%, 8%, 0.58) 44%,
    white 68%,
    white
  );
  background-position: 0 top;
  background-repeat: repeat-x;
  background-size: 100% 100%;
  top: 100px;
  bottom: -1px;
  height: 700px;
  opacity: 1;
  top: 80%;
  width: 100%;
}
.vignette-layer {
  left: 0;
  position: absolute;
  right: 0;
  z-index: 8;
}
.collection-name {
  text-align: left;
  font-weight: 400;
  padding-left: 15px;
  color: black;
}

.new-movies-title {
  text-align: left;
  font-weight: 400;
  padding-left: 15px;
  color: white;
}
</style>