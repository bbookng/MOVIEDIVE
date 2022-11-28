<template>
  <div class="movie-item d-flex flex-column justify-content-start">
    <div>
      <img @click="fetchMovie(movie.pk)" type="button" data-bs-toggle="modal" data-bs-target="#movieDetail" class="movie-list-poster" :src=imgURL alt="">
    </div>
    <p style="text-align:left; padding-left: 15px; width: 22rem;">{{ movie.title }}</p>
  </div>
</template>


<script>
// import MovieDetail from '@/components/movies/MovieDetail.vue'
import { mapActions  } from 'vuex';

export default {
  name: 'MovieListItem',
  props: {
    movie: Object
  },
  components: {
    // MovieDetail,
  },
  data() {
    return {
      imgURL: `https://image.tmdb.org/t/p/original/${ this.movie.backdrop_path }`
    }
  },
  methods: {
    ...mapActions(['fetchMovie'])
  }
}
</script>

<style scoped>
  #movieDetail {
    z-index: 20;
    margin:0;
  }
  /* .movie-item {
    max-width: 205px;
  } */
  .movie-list-poster{
    border-radius: 10px;
    width: 22rem;
    display: block;
  }
</style>