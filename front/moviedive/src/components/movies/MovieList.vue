<template>
  <div class="movie-list">
    <h3>Movie List</h3>
    <span>
      <!-- <vueper-slides
        class="no-shadow"
        :visible-slides="3"
        :slide-ratio="1 / 4"
        :dragging-distance="70">
        <vueper-slide v-for="movie in movies" :key="movie.id">
          {{ movie }}
          <MovieListItem
            :movie="movie"
          />
        </vueper-slide>
      </vueper-slides> -->

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
// import { VueperSlides, VueperSlide } from 'vueperslides'
// import 'vueperslides/dist/vueperslides.css'
import MovieListItem from '@/components/movies/MovieListItem.vue'
export default {
  props:{
    movies: Array,
    new_movies: Array
  },
  name: 'MovieList',
  components: {
    // VueperSlides, 
    // VueperSlide,
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