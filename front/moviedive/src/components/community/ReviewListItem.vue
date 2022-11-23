<template>
  <div>
    <div id="review-header">
      <div id="review-header-left">
        <h5>{{ review.movie_title }}</h5>
        <span><img src="" alt="좋아요">{{ review.like_reviews_count }}</span>
        <span><img src="" alt="댓글">{{ review.comment_count }}</span>
      </div>
      <div id="review-header-right">
        <router-link class="comment-user" :to="{ name: 'mypage', params: { username: review.user.username} }">
          <img class="user-profile-img" :src=review.user.profile_img alt="">
        </router-link>
        <div>
          <router-link class="comment-user" :to="{ name: 'mypage', params: { username: review.user.username} }">{{ review.user.nickname }}</router-link>
          {{ review.created_string }}
        </div>
      </div>
    </div>
    <br>
    <router-link
      :to="{ name: 'review_detail', params: { movieId: this.review.movie, reviewId: this.review.id }}"
    >
    {{ review.title }}</router-link>
    <p></p>
    <p>{{ review.content }}</p>
    <!-- 좋아요 수 -->
    <!-- 댓글 수 -->
    <!-- 프로필 사진 -->
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
.user-profile-img {
  width: 10%;
  height: 10%;
}

</style>