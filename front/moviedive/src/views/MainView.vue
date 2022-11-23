<template>
  <div>
    <MainTrailer/>
    <div style="margin:0 3rem 0 3rem; color:white;">
      <MovieList class="overlay" :new_movies="new_movies"/>
      <MovieList :new_movies="new_movies"/>
      <MovieList :new_movies="new_movies"/>
      <MovieList :new_movies="new_movies"/>
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
        console.log(res.data)
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
  top:80%;
}
</style>