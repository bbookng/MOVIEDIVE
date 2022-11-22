<template>
  <div>
    <h1>User Review</h1>
    <div class="d-flex justify-content-center" v-for="review in reviews" :key="review.id">
      <router-link
      class="review-list"
      :to="{ name: 'review_detail', params: { movieId: review.movie.id, reviewId: review.id }}"
      >{{ review.content }} 
      </router-link>
      {{ review.movie.title }}
      
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'UserReview',
    data() {
      return {
        reviews: null,
      }
    },
    props: {
      user: Object,
    },
    methods: {
      getReviews(username) {
        axios({
          method: 'get',
          url: this.$store.state.API_URL + `/accounts/profile/${username}/reviews/`,
          headers: this.$store.getters.authHeader
        })
        .then((res) => {
          console.log(res.data)
          this.reviews = res.data.reviews
        })
      }
    },
    created() {
      this.getReviews(this.user.username)
    }

}
</script>

<style>
.review-list {
  text-decoration: none;
  color: black;
}

</style>