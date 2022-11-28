<template>
  <div id="search-results mx-0">
    <h2 id="search-string">"{{ keyword }}"(으)로 검색한 결과</h2>
    <div class="d-flex justify-content-center">
      <div class="col-8">
        <searched-movie-list></searched-movie-list>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import SearchedMovieList from '@/components/search/SearchedMovieList'

export default {
  name: "SearchResultView",
  data() {
    return {
      keyword: this.$route.params.keyword,
    }
  },
  components:{
    SearchedMovieList
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  methods: {
    ...mapActions(['fetchMovies']),
  },
  created() {
    this.fetchMovies(this.keyword)
  }

}
</script>

<style scoped>
#search-results {
  color:rgb(0, 0, 0);
  padding: 50px;
  width: 100rem;

}
#search-string {
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 30px;
  margin-top: 30px;
}
.result-label{
  margin-top:30px; 
  margin-bottom:10px;
  padding-left:20px; 
  font-size: 25px;
}
</style>