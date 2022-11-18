<template>
  <div>
    <h1>Detail</h1>
    <p>{{ review?.movie_title }}</p>
    <p>글 번호 : {{ review?.id }}</p>
    <p>제목 : {{ review?.title }}</p>
    <p>내용 : {{ review?.content }}</p>
    <p>작성시간 : {{ review?.created_at }}</p>
    <p>수정시간 : {{ review?.updated_at }}</p>
    <button
      @click="goToReviewForm"
    >수정</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api'

export default {
  name: 'DetailView',
  data() {
    return {
      review: null,
    }
  },
  created() {
    this.getReviewDetail()
  },
  methods: {
    getReviewDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/community/${this.$route.params.movieId}/${this.$route.params.reviewId}`
      })
        .then((res) => {
          console.log(res)
          this.review = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goToReviewForm() {
      this.$router.push({ name: 'review_form', params: { movie_id: this.review.movie, review_id: this.review.id }})
    },
  }
}
</script>
