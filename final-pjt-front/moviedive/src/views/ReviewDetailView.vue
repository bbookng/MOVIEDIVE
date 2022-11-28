<template>
  <div id="review-detail-box" v-if="review">
    <div id="review-detail-top">
      <div class="d-flex align-items-center">
        <img id="film-img" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/clapperboard.png" alt="">
        <h5 class="my-0">{{ movie_title }}</h5>
      </div>
      <div id="review-title">
        <h2>{{ review?.title }}</h2>
      </div>
      <div class="d-flex justify-content-between">
        <div class="d-flex align-items-center">
          <img class="user-profile-img" :src=writerProfileImg alt="...">
          <p class="user-nickname my-0">{{ user.nickname }}</p>
          <p class="created-date my-0">{{ $moment(review.created_at).format('YYYY.MM.DD HH:mm') }}</p>
        </div>
        <div id="review-update-delete" class="d-flex align-items-end" v-if="isMe">
          <button class="review-button" @click="updateReview">수정</button>
          <button class="review-button" @click="deleteReview">삭제</button>
        </div>
    </div>
    <hr>

    </div>
    <div id="review-content">
      <div id="review-content-body">
        {{ review?.content }}
      </div>
      <div id="review-like-comment" class="d-flex align-items-center">
        <div class="review-detail-button" @click="likeReview">
          <img v-if="!userLike" class="button like" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/icon/heart+(3).png" alt="">
          <img v-if="userLike" class="button like" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/icon/heart+(2).png" alt="">
          좋아요
      </div>
      <div class="review-detail-button" @click="goCommentsList">
        <img class="button comment" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/comment.png" alt="">
        댓글
      </div>
      </div>
    </div>
    <hr>
      <div id="comment-box">
        <div class="d-flex justify-content-start" id="comments-list" v-for="comment in comments" :key="comment.id">
          <div>
            <img class="user-profile-img" :src=currentUserProfileImg alt=" user 프로필 이미지">
          </div>
          <div class="d-flex justify-content-between" style="padding:5px; width:100%;">
            <div id="comment-info" class="d-flex flex-column align-items-start">
              <p class="my-0 fw-bold py-1">{{ comment.user.nickname }}</p>
              <p class="my-0">{{ comment.content }}</p>
            </div>
            <div>
              <p class="my-0">{{ comment.created_string }}</p>
            </div>
          </div>
        </div>
        <div id="comment-create-form">
          <form class="d-flex justify-content-center align-items-center" @submit.prevent="createComment">
            <input id="comment-input" v-model="comment_content" type="text" placeholder="리뷰에 댓글 남기기" />
            <input id="comment-button" class="btn btn-outline-dark-sm" type="submit" value="등록">
          </form>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'https://moviedive.co.kr/api'

export default {
  name: 'DetailView',
  data() {
    return {
      review: null,
      user: null,
      comment_content: null,
      isMe: true, 
      movie_title: null,
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
    },
    userLike() {
      return this.review.like_users.find((lu) => {
        return lu == this.currentUser.id
      }) ? true : false
    }


  },
  created() {
    this.getReviewDetail()
    this.getMovieTitle()
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
      const API_URL = 'https://moviedive.co.kr/api'
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
      const API_URL = 'https://moviedive.co.kr/api'
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
    },
    getMovieTitle() {
      const API_URL = 'https://moviedive.co.kr/api'
      axios({
        url: `${API_URL}/movies/${this.$route.params.movieId}/`,
        method: 'get',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.movie_title = res.data.title
      })

    },
    goCommentsList() {
      // 댓글 div 로 이동
      const commentbox = document.getElementById("comments-list")
      commentbox.scrollIntoView({behavior: 'smooth'})
    },
  }
}
</script>

<style scoped>
#comment-info {
  display: inline-block;
}
#comment-create-form {
  border-top: 1px solid rgba(126, 123, 123, 0.662);
  padding-bottom: 10px;
  padding-top: 10px;

}
.review-detail-button {
  margin-right: 10px;
}
.review-detail-button .button {
  width: 40px;
  height: 40px;
} 

#review-content {
  margin-left: 10%;
  margin-right: 10%;
}

.review-icon-img {
  width: 5%;
  height: 5%;
}

#review-content-body {
  line-height: 28.7px;
  margin-bottom: 3rem;
  text-align: left;
}

.user-nickname {
  font-size: 20px;
  margin-right: 10px;
  font-weight: 600;
}

#comments-list {
  border-top: 1px solid rgba(126, 123, 123, 0.662);
}

#comment-box {
  margin-top: 3%;
  margin-left: 15%;
  margin-right: 15%;
}

.created-date {
  font-size: 15px;

}

#review-detail-box {
  margin-top: 2rem;
  margin-left: 15%;
  margin-right: 15%;
}

#film-img {
  width: 4%;
  height: 4%;
}

.user-profile-img {
  width: 60px;
  height: 60px;
  border: none;
  border-radius: 50%;
}

#review-detail-top {
  text-align: left;
  margin-bottom: 2rem;
}

#review-title {
  margin-left: 5px;
  margin-top: 5px;
}

.review-button{
  border: none;
  background-color: transparent;
}

#review-update-delete {
  padding-right: 15px;
}

#comment-input {
  width: 500px;
  height: 35px;
  border-radius: 10px;
  border: none;
  background-color: rgba(220, 220, 220, 0.322);
  padding: 1rem;
}

</style>