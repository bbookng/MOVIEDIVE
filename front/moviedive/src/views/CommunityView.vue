<template>
  <div class="page">
    <form @submit="searchThings(searchKeyword)">
        <div class="search-box">
          <div class="search-container">
            <input autocomplete="off" @input="changeKeyword" :value="searchKeyword" type="search" id="search" placeholder="영화 이름으로 검색" />
            <auto-complete-suggestions id="suggestion-box" @titleFromSuggestions="fillSearchKeyword"></auto-complete-suggestions>
          </div>
        </div>
      </form>
    <button
      @click="goToReviewCreate"
    >리뷰 작성하기</button>
    <hr>
    <ReviewList :movie="movie"/>
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList'
import { mapActions } from 'vuex'
import AutoCompleteSuggestions from '@/components/AutoCompleteSuggestions'

export default {
  name: 'CommunityView',
  components: {
    ReviewList,
    AutoCompleteSuggestions,
  },
  data() {
    return{
      searchKeyword: '',
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  created() {
    this.getReviews()
  },
  methods: {
    getReviews() {
      if (this.isLoggedIn == true) {
        this.$store.dispatch('getReviews')
      } else {
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push({ name: 'LogInView' })
      }
    },
    goToReviewCreate() {
      this.$router.push({ name: 'create_review' })
    },
    ...mapActions(['fetchMovies', 'searchCollections', 'autoComplete']),
    searchThings(keyword) {        
      this.$router.push({ name: 'search_result', params: { keyword } })
    },
    fillSearchKeyword(suggest){
      this.searchKeyword = suggest.title
      this.movie = suggest.id
    },
    changeKeyword(event) {
      this.searchKeyword = event.target.value
      this.autoComplete(this.searchKeyword)
    },
  }
}
</script>

<style>
.page {
  margin: 0 2em;
}
</style>