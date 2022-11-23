<template>
  <div v-if="review">
    <div>
      <p>{{ review?.movie_title }}</p>
    <p>{{ review?.title }}</p>
    <div >
      <img :src=writerProfileImg alt="...">
      {{ user.nickname }}
      {{ $moment(review.created_at).format('YYYY.MM.DD HH:mm') }}
    </div>
    <hr>

    </div>
    <div>
      <div>
        {{ review?.content }}
      </div>
      <div>
        <button @click="likeReview">좋아요</button>
        <button>댓글</button>
        <button>공유</button>
      </div>
      <hr>
      <div>
        <div id="comments-list" v-for="comment in comments" :key="comment.id">
          <div>
            <img :src=currentUserProfileImg alt=" user 프로필 이미지">
          </div>
          <div>
            {{ comment.user.nickname }}
            {{ comment.content }}
          </div>
        </div>
        <div>
          <form @submit.prevent="createComment">
            <input v-model="comment_content" type="text" placeholder="리뷰에 댓글 남기기" />
            <input type="submit">
          </form>
        </div>
      </div>
    </div>
    <div v-if="isMe">
      <button @click="updateReview">수정</button>
      <button @click="deleteReview">삭제</button>
    </div>
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
      user: null,
      comment_content: null,
      isMe: true, 
    }
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser
    },
    comments() {
      return this.review.community_comments
    },
    writerProfileImg() {
      return this.review.user.profile_img
    },
    currentUserProfileImg() {
      return this.currentUser.profile_img
    }


  },
  created() {
    this.getReviewDetail()
  },
  methods: {
    getReviewDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/community/${this.$route.params.movieId}/${this.$route.params.reviewId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.review = res.data
          this.user = res.data.user
        })
        .then(()=>{
          this.checkUser()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview() {
      if (confirm('정말 삭제하시겠습니까?') == true) {
        axios({
        method: 'delete',
        url: `${API_URL}/community/${this.$route.params.movieId}/${this.$route.params.reviewId}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      
      })
        .then(() => {
            this.$router.push({ name: 'community' })
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    updateReview() {
      this.$router.push({ name: 'create_review', query: this.review })
    },
    likeReview() {
      const API_URL = 'http://127.0.0.1:8000/api'
      axios({
        url: `${API_URL}/community/${this.$route.params.movieId}/${this.$route.params.reviewId}/like/`,
        method: 'post',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => { 
        this.getReviewDetail()
        console.log(res.data)
      })
    },
    createComment() {
      const API_URL = 'http://127.0.0.1:8000/api'
      const content = this.comment_content

      if (!content) {
        alert('내용을 입력해주세요')
        return
      } 

      axios({
        url: `${API_URL}/community/${this.$route.params.movieId}/${this.$route.params.reviewId}/comments/create/`,
        method: 'post',
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.getReviewDetail()
        this.comment_content = null
        console.log(res.data)
      })

    },
    checkUser() {
      if (this.currentUser.id == this.user.id) {
        return this.isMe = true
      } else {
        return this.isMe = false
      }
    }
  }
}
</script>

<style>
img {
  height: 10%;
  width: 10%;
}
</style>