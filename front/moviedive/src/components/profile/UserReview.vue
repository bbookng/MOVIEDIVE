<template>
  <div>
    <div class="d-flex justify-content-center" v-for="review in reviews" :key="review.id">
      <div id="review" class="d-flex justify-content-between align-items-center">
          <router-link
          class="review-list"
          :to="{ name: 'review_detail', params: { movieId: review.movie.id, reviewId: review.id }}"
          >{{ review.content }} 
        </router-link>
        {{ review.movie.title }}  
      </div>
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

#review {
  border: 1px black solid;
  border-radius: 20px;
  width: 40rem;
  height: 40px;
}

</style>