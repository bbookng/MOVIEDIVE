<template>
  <div class="container">
    <div class="row" v-for="movie in movies" :key="movie">
      <UserMovieListItem class="col" :movie="movie"/>
    </div>
    <MovieDetail/>

  </div>
</template>

<script>
import axios from 'axios';
import MovieDetail from '@/components/movies/MovieDetail.vue'
import UserMovieListItem from '@/components/profile/UserMovieListItem.vue'

export default {
    name: 'UserLikesMovies',
    components: {
      MovieDetail,
      UserMovieListItem,
    },
    data() {
      return {
        movies: null,
      }
    },
    props: {
      user: Object,
    },
    methods: {
      getMovies(username) {
        axios({
          method: 'get',
          url: this.$store.state.API_URL + `/accounts/profile/${username}/movies/`,
          headers: this.$store.getters.authHeader
        })
        .then((res) => {
          console.log(res.data)
          this.movies = res.data.like_movies
        })
      }
    },
    created() {
      this.getMovies(this.user.username)
    }

}
</script>

<style>

</style>