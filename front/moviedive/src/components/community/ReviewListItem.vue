<template>
  <div id="review-list-item" class="d-flex flex-column justify-content-between align-items-center" style="border-bottom: 1px solid gray; width: 100%;">
    <!-- 헤더 -->
    <div id="review-header" class="d-flex flex-row justify-content-between" style="width:100%; height:20rem;" >
      <div id="review-header-left" class="d-flex flex-row">
        <h5>{{ review.movie_title }}</h5>
        <span><img src="" alt="좋아요">{{ review.like_reviews_count }}</span>
        <span><img src="" alt="댓글">{{ review.comment_count }}</span>
      </div>
      <div id="review-header-right" class="d-flex justify-content-end">
        <router-link class="comment-user" style="width:50px; height:50px; border-radius:70%; overflow: hidden;" :to="{ name: 'mypage', params: { username: review.user.username} }">
          <img class="user-profile-img" style="width:100%; height:100%; object-fit:cover;" :src=review.user.profile_img alt="">
        </router-link>
        <div>
          <router-link class="comment-user" :to="{ name: 'mypage', params: { username: review.user.username} }">{{ review.user.nickname }}</router-link>
          {{ review.created_string }}
        </div>
      </div>
    </div>
    <!-- 타이틀과 컨텐츠 -->
    <router-link :to="{ name: 'review_detail', params: { movieId: this.review.movie, reviewId: this.review.id }}">{{ review.title }}</router-link>
    <p>{{ review.content }}</p>
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
#review-list-item {
  padding: 5rem 5rem 5rem 5rem;
}

.user-profile-img {
  width: 10%;
  height: 10%;
}

</style>