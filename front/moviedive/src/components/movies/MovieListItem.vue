<template>
  <div class="movie-item swiper-slide">
    <div>
      <img type="button" data-bs-toggle="modal" data-bs-target="#movieDetail" class="movie-list-poster" :src=imgURL alt="">
    </div>
    <p style="padding-left:15px;">{{ movie.title }}</p>
    <MovieDetail
      class="modal fade" id="movieDetail" tabindex="-1" aria-labelledby="movieDetail" aria-hidden="true"
      :movie="movie"
    />
    <SwiperSlide></SwiperSlide>
  </div>
</template>


<script>
import MovieDetail from '@/components/movies/MovieDetail.vue'
import { SwiperSlide } from 'swiper/vue';

export default {
  name: 'MovieListItem',
  props: {
    movie: Object
  },
  components: {
    MovieDetail,
    SwiperSlide,
  },
  data() {
    return {
      imgURL: `https://image.tmdb.org/t/p/original/${ this.movie.backdrop_path }`
    }
  },
}
</script>

<style scoped>
  #movieDetail {
    z-index: 100;
  }
  .movie-item {
    max-width: 300px;
  }
  .movie-list-poster{
    border-radius: 10px;
    padding: 5px;
    width: 22rem;
    display: block;
  }
  /* SWIPER */
  .swiper-slide {
  transition: all 300ms ease-in-out;
  border-radius: 5px;
  }
  
.swiper-slide img {
  border-radius: 5px;
  max-width: 18rem;
  cursor: grab;
}

.swiper-slide img:active {
  cursor: grabbing;
}

.swiper-slide:hover {
  transform: scale(1.5);
  transition: all 300ms ease-in-out;
  transition-delay: 300ms;
  z-index: 1;
}

.swiper-slide:hover img {
  transition-delay: 300ms;
  box-shadow: 0 0 5px 1px rgba(0,0,0,0.5);
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