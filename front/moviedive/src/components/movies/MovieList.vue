<template>
  <div class="movie-list">
    <h3>Movie List</h3>
    <span>
      <MovieListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"/>
      <MovieListItem
      v-for="movie in new_movies"
      :key="movie.id"
      :movie="movie"/>
    </span>
    
  </div>
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem.vue'
export default {
  props:{
    movies: Array,
    new_movies: Array
  },
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {

  }


}
</script>

<style>
.movie-list {
  text-align: start;
}

</style>