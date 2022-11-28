<template>
  <div class="d-flex flex-column justify-content-start" style="width: 100vw">
    <carousel
      id="mlc"
      :perPage="6"
      :scrollPerPage="true"
      :navigationEnabled="false"
      :paginationEnabled="false"
    >
      <slide
        id="movie-list-slide"
        class="label mx-0"
        v-for="movie in movies"
        :key="movie.pk"
        :movie="movie"
      >
        <MovieListItem
          data-bs-toggle="modal"
          data-bs-target="#movieDetail"
          :movie="movie"
        />
      </slide>
    </carousel>
  </div>
</template>

<script>
import MovieListItem from "@/components/movies/MovieListItem";
import { Carousel, Slide } from "vue-carousel";

export default {
  name: "MovieList",
  props: {
    movies: Array,
  },
  components: {
    MovieListItem,
    Carousel,
    Slide,
  },
};
</script>

<style scoped>

#mlc {
  width: 100%;
}
</style>