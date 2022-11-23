<template>
  <div>
    <div class="overlay meta-layer">
      <div><h3 class="collection-name">이 달의 신작 영화</h3></div>
      <div class="movie-container"> 
        <MovieListItem
        v-for="movie in new_movies"
        :key="movie.id"
        :movie="movie"/>
      </div>
    </div>   
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

<style scoped>
.movie-container {
  text-align: start;
  display: flex;
  flex-direction: row;
}
.collection-name {
  text-align: left;
}
.overlay {
  transition: transform 1.5s cubic-bezier(.165,.84,.44,1);
  width: 100%;
}
</style>