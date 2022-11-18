<template>
  <div>
    <h1>리뷰 작성</h1>
    <form @submit.prevent="createReview">
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

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewCreateView',
  data() {
    return {
      movie: null,
      title: null,
      content: null,
      rate: null,
    }
  },
  methods: {
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

</style>
