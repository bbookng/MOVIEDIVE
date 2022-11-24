<template>
  <div>
    <div class="movie-container">
      <div><h3 class="collection-name">이 달의 신작 영화</h3></div>
      <swiper
        :modules="modules"
        :slides-per-view="3"
        :space-between="50"
        navigation
        :pagination="{ clickable: true }"
        :scrollbar="{ draggable: true }"
        @swiper="onSwiper"
        @slideChange="onSlideChange">
        <div class="swiper-container"> 
          <div class="swiper-wrapper">
            <MovieListItem
              v-for="movie in new_movies"
              :key="movie.id"
              :movie="movie"/>
            <div class="swiper-button-next"></div>
            <div class="swiper-button-prev"></div>
          </div>
        </div>
      </swiper>
    </div>   
  </div>
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem.vue'
import { Navigation, Pagination, Scrollbar, A11y } from 'swiper';
import { Swiper } from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';

export default {
  props:{
    movies: Array,
    new_movies: Array
  },
  name: 'MovieList',
  components: {
    MovieListItem,
    Swiper,
  },
  mounted() {
    this.init()
  },
  methods: {
    init() {
      const onSwiper = (swiper) => {
        console.log(swiper);
      };
      const onSlideChange = () => {
        console.log('slide change');
      };
      const swiper = new Swiper(".swiper-container", {
        centeredSlides: true,
        loop: true,
        navigation: {
              nextEl: '.swiper-button-next',
              prevEl: '.swiper-button-prev',
            },
        })
      return {
        onSwiper,
        onSlideChange,
        swiper,
        modules: [Navigation, Pagination, Scrollbar, A11y],
      };
      
    }
  }


}
</script>

<style scoped>
.swiper-container {
  text-align: start;
  /* display: flex;
  flex-direction: row; */
  overflow: visible;
}
.collection-name {
  text-align: left;
  font-weight: 400;
  padding-left: 5px;
}
@media screen and (max-width: 599px) {
  .swiper-slide img {
    max-width: 14rem;
  }
  .swiper-button-next,
  .swiper-button-prev {
    display: none;
  }
}

@media screen and (max-width: 400px) {
  .swiper-slide img {
    max-width: 10.5rem;
    border-radius: 2px;
  }
}
</style>