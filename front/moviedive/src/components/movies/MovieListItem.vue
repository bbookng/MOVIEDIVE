<template>
  <div>
    <p>{{ movie.title }}</p>
    <div>
      <img type="button" data-bs-toggle="modal" data-bs-target="#movieDetail" class="movie-list-poster" :src=imgURL alt="">
    </div>
    <MovieDetail
      class="modal fade" id="movieDetail" tabindex="-1" aria-labelledby="movieDetail" aria-hidden="true"
      :movie="movie"
    />
    <hr>

    
  </div>
</template>

<script>
import MovieDetail from '@/components/movies/MovieDetail.vue'

export default {
  name: 'MovieListItem',
  props: {
    movie: Object
  },
  components: {
    MovieDetail
  },
  data() {
    return {
      imgURL: `https://image.tmdb.org/t/p/original/${ this.movie.backdrop_path }`
    }
  },
}
</script>

<style scoped>
  .movie-list-poster{
    border-radius: 10px;
    padding: 5px;
    width: 100%;
    display: block;
  }
  .movie-list-poster:hover { 
    transform: translateY(-10px);
    transform: scale(1.02);
    overflow: visible;
    filter: drop-shadow(0 0 0.2rem #ffffff);
    transition: 0.3s;
    opacity: 0.8;
  }

.img-box {
    padding-top:0.15rem;
  }
</style>