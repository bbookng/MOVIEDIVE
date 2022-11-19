<template>
  <div>
    {{ currentUser }}
    <div>
      {{ profileImg }}
      <img :src=profileImg alt="프로필 이미지 넣자">
      <div>
        <div>
          {{ currentUser.nickname }}
          <button>팔로우</button>
        </div>
        <div>
          {{}}

        </div>
        <div>
          {{ currentUser.message }}
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
export default {
  name: 'MyPageView',
  computed: {
    currentUser() {
      return this.$store.getters.currentUser
    },
    profileImg() {
      return this.currentUser.profile_img
    }
  },
  methods: {

  },
  created() {

  }

}
</script>

<style>

</style>