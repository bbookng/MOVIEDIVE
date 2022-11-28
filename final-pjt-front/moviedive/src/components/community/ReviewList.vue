<template>
  <div class="review-list" style="width:100%">
    <div v-if="!movie">
      <ReviewListItem
        v-for="review in reviews"
        :key="review.id"
        :review="review"
      />
    </div>

    <div v-if="movie">
      <ReviewListItem
        v-for="review in search_reviews"
        :key="review.id"
        :review="review"
      />
    </div>

  </div>
</template>

<script>
import ReviewListItem from '@/components/community/ReviewListItem'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem
  },
  props: {
    movie: Number
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    },
    search_reviews() {
      return this.reviews.filter(review => review.movie == this.movie)
    }
  }
}
</script>

<style>
.review-list {
  text-align: start;
  background-color: white;
}
</style>