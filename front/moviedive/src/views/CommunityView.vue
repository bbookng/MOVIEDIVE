<template>
  <div class="d-flex align-items-center">
    <div class="d-flex flex-column justify-content-start align-items-center page">
      <div class="d-flex justify-content-between" style="border-bottom:1px solid gray; width:100%; padding:1rem 2rem 1rem 2rem; background:#e2e2e2;">
        <form @submit.prevent style="width: 50rem; height: 3.5rem;">
          <div class="search-box" style="width: 50rem; height: 3.5rem;">
            <div class="search-container" style="width: 50rem; height: 3.5rem;">
              <input autocomplete="off" @input="changeKeyword" :value="searchKeyword" type="search" id="search" placeholder="🔍  영화 이름으로 리뷰 검색" />
              <auto-complete-suggestions id="suggestion-box" @titleFromSuggestions="fillSearchKeyword"></auto-complete-suggestions>
            </div>
          </div>
        </form>
        <button
          @click="goToReviewCreate"
          style="border:1px solid gray; background:white; font-weight: 100;"
        >리뷰 작성</button>
      </div>
    <ReviewList id="review-list" :movie="movie"/>
  </div>
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList'
import { mapActions } from 'vuex'
import AutoCompleteSuggestions from '@/components/community/AutoCompleteSuggestions'

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

<style scoped>
.page {
  margin: 0 25rem 0 25rem;
  width: 1216px;
  border-right: 1px solid gray;
  border-left: 1px solid gray;
}

  /* search box */
  .search-container input#search{
    width: 50rem;
    height: 3.5rem;
    float: right;
    transition: width .55s ease;
    border-radius: 0px;
    border-radius: 50px;
    border: 1px solid gray;
    text-align: center;
  }
  input::placeholder {
    color: #cacaca;
  }
  .search-container input#search:-ms-input-placeholder {  
    color: white; 
  }  
  .search-container input#search:focus, .search-container input#search:active{
    outline:none;
    width: 100%;
  }

</style>