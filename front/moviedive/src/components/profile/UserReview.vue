<template>
  <div>
    <h1>User Review</h1>
    <div v-for="review in reviews" :key="review.id">
      <router-link
      :to="{ name: 'review_detail', params: { movieId: review.movie.id, reviewId: review.id }}"
      >{{ review.content }} {{ review.movie.title }}
      </router-link>
      
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

</style>