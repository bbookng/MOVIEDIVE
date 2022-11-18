<template>
  <div class="review-list">
    <ReviewListItem
      v-for="review in reviews"
      :key="review.id"
      :review="review"
    />
  </div>
</template>

<script>
import ReviewListItem from '@/components/community/ReviewListItem'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    }
  }
}
</script>

<style>
.review-list {
  text-align: start;
}
</style>