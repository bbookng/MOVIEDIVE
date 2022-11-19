<template>
  <div>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'

export default {
  name: 'MainView',
  components: {
    MovieList
  },
  computed:{
        movies() {
      return this.$store.state.movies
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }

}
</script>

<style>

</style>