<template>
  <div>
    <h5>{{ review.movie_title }}</h5>
    <p>{{ review.username }}</p>
    <router-link
      :to="{ name: 'review_detail', params: { movieId: this.review.movie, reviewId: this.review.id }}"
    >
    {{ review.title }}</router-link>
    <p></p>
    <p>{{ review.content }}</p>
    <!-- 좋아요 수 -->
    <!-- 댓글 수 -->
    <!-- 프로필 사진 -->
    <p>{{ review.created_string }}</p>
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