<template>
  <div>
    <h1 v-if="!review_id">리뷰 작성</h1>
    <h1 v-if="review_id">리뷰 수정</h1>
    <form @submit.prevent="saveReview">
      <form v-if="!review_id" @submit.prevent>
        <div class="search-box">
          <div class="search-container">
            <input autocomplete="off" @input="changeKeyword" :value="searchKeyword" type="search" id="search" placeholder="영화 이름으로 검색" />
            <auto-complete-suggestions id="suggestion-box" @titleFromSuggestions="fillSearchKeyword"></auto-complete-suggestions>
          </div>
        </div>
      </form>
      <p v-if="movie_id">{{ movie_title }}</p>
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <label for="rate">별점 </label>
      <input type="number" name="rate" v-model="rate" min="0" max="5" step="0.5"><br>
      <input type="submit" id="submit" value="발행">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import AutoCompleteSuggestions from '@/components/AutoCompleteSuggestions'

const API_URL = 'https://moviedive.co.kr'

export default {
  
  name: 'ReviewFormView',
  data() {
    return {
      searchKeyword: '',
      movie: null,
      title: null,
      content: null,
      rate: null,

      requestBody: this.$route.query,
      review_id: this.$route.query.id,
      movie_id: this.$route.query.movie,
      movie_title: this.$route.query.movie_title,
    }
  },
  components: {
    AutoCompleteSuggestions
  },
  mounted() {
    this.getUpdateDetail()
  },
  methods: {
    getUpdateDetail() {
      if (this.review_id !== undefined) {
        axios({
        method: 'GET',
        url: `${API_URL}/api/community/${this.movie_id}/${this.review_id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.movie = res.data.movie
          this.title = res.data.title
          this.content = res.data.content
          this.rate = res.data.rate
        })
        .catch((err) => {
          console.log(err)
        })
      }
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
    saveReview() {
      const id = this.review_id
      const movie = this.movie
      const title = this.title
      const content = this.content
      const rate = this.rate

      if (!movie) {
        alert('영화를 선택해주세요')
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

      if (this.review_id === undefined) {
        axios({
        method: 'post',
        url: `${API_URL}/api/community/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: { 
          id: id,
          movie: movie,
          title: title,
          content: content,
          rate: rate
        }
        })
          .then(() => {
            alert('생성 완료!')
            this.$router.push({ name: 'community' })
          })
          .catch((err) => {
            console.log('에러가 생성 axios 요청에서')
            console.log(err)
          })
      } else {
        axios({
        method: 'put',
        url: `${API_URL}/api/community/${ this.movie_id }/${ this.review_id }/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          id: id,
          movie: movie,
          title: title,
          content: content,
          rate: rate
        }
      })
        .then(() => {
          alert('수정 완료!')
          this.$router.push({ name: 'community' })
        })
        .catch((err) => {
          console.log('에러가 수정 axios 요청에서')
          console.log(err)
        })
      }

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
