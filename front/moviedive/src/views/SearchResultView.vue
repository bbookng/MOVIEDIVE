<template>
  <div id="search-results">
    <h2 id="search-string">"{{ keyword }}"(으)로 검색한 결과</h2>
    <div class="row">
      <div class="col-12 result-label">
        {{ movies }}
        영화
      </div>
      <div class="col-12">
        <searched-movie-list></searched-movie-list>
      </div>
      <div class="col-12 result-label">
        컬렉션
      </div>
      <div class="col-12">
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
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
    ...mapGetters(['movies']),
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
/* #search-results {
  color:white;
  padding: 50px;
}
#search-string {
  font-size: 30px;
  font-weight: bold;
}
.result-label{
  margin-top:30px; 
  margin-bottom:10px;
  padding-left:20px; 
  font-size: 25px;
} */
</style>