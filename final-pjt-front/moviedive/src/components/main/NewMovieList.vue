<template>
  <div>
    <MovieListCarousel :movieList="newMovieList"/>
  </div>
</template>

<script>
import MovieListCarousel from '@/components/main/MovieListCarousel.vue';

export default {
    name:'NewMovieList',
    components: {
        MovieListCarousel,
    },
    computed:{
        newMovieList() {
            return this.$store.state.newmovielist
        }
    },
    methods:{

    },

}
</script>

<style>

</style>