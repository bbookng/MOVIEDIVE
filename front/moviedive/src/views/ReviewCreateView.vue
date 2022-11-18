<template>
  <div>
    <h1>리뷰 작성</h1>
    <form @submit.prevent="createReview">
      <form @submit="searchThings(searchKeyword)">
        <div class="search-box">
          <div class="search-container">
            <input autocomplete="off" @input="changeKeyword" :value="searchKeyword" type="search" id="search" placeholder="영화 이름으로 검색" />
            <auto-complete-suggestions id="suggestion-box" @titleFromSuggestions="fillSearchKeyword"></auto-complete-suggestions>
          </div>
        </div>
      </form>
      <!-- <input type="text" id="movie" v-model.trim="movie"><br> -->
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import AutoCompleteSuggestions from '@/components/AutoCompleteSuggestions'

const API_URL = 'http://127.0.0.1:8000'

export default {
  
  name: 'ReviewCreateView',
  data() {
    return {
      movie: null,
      title: null,
      content: null,
      rate: null,
      searchKeyword: '',
    }
  },
  components: {
    AutoCompleteSuggestions
  },
  methods: {
    ...mapActions(['fetchMovies', 'searchCollections', 'autoComplete']),
    searchThings(keyword) {        
      this.$router.push({ name: 'search_result', params: { keyword } })
    },
    fillSearchKeyword(keyword){
      this.searchKeyword = keyword
    },
    changeKeyword(event) {
      this.searchKeyword = event.target.value
      this.autoComplete(this.searchKeyword)
    },
    createReview() {
      const movie = this.movie
      const title = this.title
      const content = this.content
      const rate = this.rate
      if (!movie) {
        alert('영화를 입력해주세요')
        return
      } else if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      } else if (!rate) {
        alert('평점을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/community/`,
        data: {
          movie: movie,
          title: title,
          content: content,
          rate: rate,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'ReviewView' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
  .search-box{
    width: 300px;
    height: 40px;
    font-size:20px;
  }
    .search-container{
    width: 300px;
    vertical-align: middle;
    white-space: nowrap;
    position: relative;
  }
  .search-icon{
    padding-right:10px;
    background:black;
    position: absolute;
    border: none;
    top: -2px;
    left:82%;
    margin-left: 17px;
    margin-top: 6px;
    z-index: 1;
    color: #FFF;
  }
  #suggestion-box {
    position:absolute;
    /* visibility: hidden; */
    left:20px;
    z-index: 5;
  }
  #suggestion-box {
    position:absolute;
    font-size:15px;
    width: 300px;
    opacity: 0;
    top:50px;
    left:20px;
    z-index: 5;
  }
  .search-container:focus-within #suggestion-box {
      opacity: 1;
  }
</style>
