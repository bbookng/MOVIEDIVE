<template>
  <div>
    <input
      type="text"
      placeholder="영화 제목으로 리뷰 검색"
    >
    <br>
    <router-link :to="{ name: 'review-create' }">[CREATE]</router-link>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList'

export default {
  name: 'CommunityView',
  components: {
    ReviewList,
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  created() {
    this.getReviews()
  },
  methods: {
    getReviews() {
      if (this.isLoggedIn == true) {
        this.$store.dispatch('getReviews')
      } else {
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push({ name: 'LogInView' })
      }
    },
  }
}
</script>

<style>

</style>