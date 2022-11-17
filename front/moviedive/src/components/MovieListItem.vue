<template>
  <div>
    <h5>{{ movie.pk }}</h5>
    <p>{{ movie.title }}</p>
    <img :src=imgURL alt="">
    <hr>
  </div>
</template>

<script>
export default {
  nmae: 'MovieListItem',
  props: {
    movie: Object
  },
  data() {
    return {
      imgURL: `https://image.tmdb.org/t/p/original/${ this.movie.backdrop_path }`
    }

  },
}
</script>

<style>

</style>