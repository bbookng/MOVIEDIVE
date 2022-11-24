<template>
  <div style="width:2160px;">
    <MainTrailer/>
    <div class="hero-vignette vignette-layer"></div>
    <div style="margin:0 3rem 0 3rem; color:white;">
      <MovieList class="overlay" style="top:80%;" :new_movies="new_movies"/>
      <MovieList class="overlay" style="top:110%;" :new_movies="new_movies"/>
      <MovieList class="overlay" style="top:140%;" :new_movies="new_movies"/>
      <MovieList class="overlay" style="top:170%;" :new_movies="new_movies"/>
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'
import MainTrailer from '@/components/main/MainTrailer.vue'
import { mapActions } from 'vuex'
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api'


export default {
  name: 'MainView',
  components: {
    MovieList,
    MainTrailer,
  },
  data() {
    return {
      new_movies: null,
    }
  },
  computed:{
    movies() {
    return this.$store.state.movies
    },
  },
  methods: {
    ...mapActions(['getMovies']),
    getNewMovies() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/new/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        this.new_movies = res.data
      })
    }

  },
  created() {
    this.getMovies()
    this.getNewMovies() 
  },

}
</script>

<style scoped>
.overlay{
  z-index: 10;
  position:absolute;
}
.hero-image-wrapper {
    bottom: 0;
    left: 0;
    position: absolute;
    right: 0;
    top: 0;
}
 er {
    left: 0;
    position: absolute;
    right: 0;
    z-index: 5;
}
.hero-vignette {
    background-color: transparent;
    background-image: linear-gradient(180deg,hsla(0,0%,8%,0) 0,hsla(0,0%,8%,.15) 15%,hsla(0,0%,8%,.35) 29%,hsla(0,0%,8%,.58) 44%,white 68%,white);
    background-position: 0 top;
    background-repeat: repeat-x;
    background-size: 100% 100%;
    bottom: -1px;
    height: 30vw;
    opacity: 1;
    top: 80%;
    width: 100%;
}
</style>