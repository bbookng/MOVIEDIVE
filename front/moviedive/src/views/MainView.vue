<template>
  <div>
    <MainTrailer/>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'
import MainTrailer from '@/components/main/MainTrailer.vue'
import { mapActions } from 'vuex'

export default {
  name: 'MainView',
  components: {
    MovieList,
    MainTrailer,
  },
  computed:{
      movies() {
      return this.$store.state.movies
    }
  },
  created() {
    this.getMovies()
    this.fetchNewMovieList()   
  },
  methods: {
    ...mapActions(['fetchNewMovieList', 'getMovies']),
  }

}
</script>

<style>

</style>