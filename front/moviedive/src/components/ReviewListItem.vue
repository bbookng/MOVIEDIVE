<template>
  <div>
    <h5>movie id: {{ review.movie }}</h5>
    <h5>review id: {{ review.id }}</h5>
    <p>{{ review.username }}</p>
    <router-link
      @click="getReviewDetail"
      :to="{ name: 'review-detail', params: { movieId: this.review.movie, reviewId: this.review.id }}"
    >
    {{ review.title }}</router-link>
    <p></p>
    <p>{{ review.content }}</p>
    <!-- 좋아요 수 -->
    <!-- 댓글 수 -->
    <!-- 프로필 사진 -->
    <!-- 작성 시간 -->
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
}
</script>

<style>

</style>