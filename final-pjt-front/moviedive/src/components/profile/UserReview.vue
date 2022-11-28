<template>
  <div>
    <div class="d-flex justify-content-center" v-for="review in reviews" :key="review.id">
      <div id="review" class="d-flex justify-content-between align-items-center px-4">
        <div id="review-title">
          <router-link
          class="review-list"
          :to="{ name: 'review_detail', params: { movieId: review.movie.id, reviewId: review.id }}"
          >{{ review.title }} 
          </router-link>
        </div>
          <div id="line"></div>
          <div class="review-movie-title">
            {{ review.movie.title }}  
          </div>
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

#review-title {
  width: 20vw;
  
}

.review-movie-title {
  width:15vw;
}

#review {
  border: 1px black solid;
  border-radius: 20px;
  width: 80%;
  height: 40px;
  font-size: 15px;
  margin: 5px;
}

#line {
  margin-left:220px;
  height: 100%;
  width: 0;
  border: 0.1px solid black;
}

</style>