<template>
  <div id="review-list-item" class="d-flex flex-column justify-content-between align-items-start" style="border-bottom: 1px solid gray; width: 100%;">
    <!-- 헤더 -->
    <div id="review-header" class="d-flex flex-row justify-content-between" style="width:100%;" >
      <div id="review-header-left" class="d-flex flex-row align-items-center">
        <h5 style="font-size:20pt; font-weight:600; margin-right:1rem; margin-bottom:0;">🎞️ {{ review.movie_title }}</h5>
        <span style="margin-right:1rem;"><img src="https://moviedive.s3.ap-northeast-2.amazonaws.com/icon/heart+(3).png" alt="좋아요" style="width:20px; padding:0;"> {{ review.like_reviews_count }}</span>
        <span style="margin-right:1rem;"><img src="https://moviedive.s3.ap-northeast-2.amazonaws.com/comment.png" alt="댓글" style="width:20px; padding:0;"> {{ review.comment_count }}</span>
      </div>
      <div id="review-header-right" class="d-flex justify-content-end">
        <router-link class="comment-user" style="margin-right:1rem; margin-top:1rem; width:50px; height:50px; border-radius:70%; overflow: hidden;" :to="{ name: 'mypage', params: { username: review.user.username} }">
          <img class="user-profile-img" style="padding:0; width:100%; height:100%; object-fit:cover;" :src=review.user.profile_img alt="">
        </router-link>
        <div style="margin-top:1rem;">
          <router-link class="comment-user" :to="{ name: 'mypage', params: { username: review.user.username } }" style="text-decoration:none; color:black; font-weight:500; font-size:15pt;">{{ review.user.nickname }}</router-link>
          <p style="font-size:12pt; margin-bottom:0;">{{ review.created_string }}</p>
        </div>
      </div>
    </div>
    <!-- 타이틀과 컨텐츠 -->
    <div>
      <router-link :to="{ name: 'review_detail', params: { movieId: this.review.movie, reviewId: this.review.id }}" style="text-decoration:none; color:black; font-weight:500; font-size:18pt;">{{ review.title }}</router-link>
      <p id="review-content" class="overflow-hidden;">{{ review.content }}</p>
    </div>

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
  padding: 1rem 3rem 1rem 3rem;
}

#review-header-left {
  margin-top: 1rem;
}

.user-profile-img {
  width: 10%;
  height: 10%;
}

#review-content {
  width: 1000px;
  margin-top: 15px;
}

</style>