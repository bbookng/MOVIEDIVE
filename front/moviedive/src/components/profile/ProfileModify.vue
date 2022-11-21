<template>
  <div>
    <div>
      <img :src=profileImg alt="프로필 이미지">
      <button>프로필 이미지 변경하기</button>
    </div>
    <div>
      <div>
        {{ currentUser.username }}
        {{ currentUser.email }}
        
      </div>
      <div>
        <p>{{ currentUser.nickname }}</p>
        <button>닉네임 변경하기</button>
      </div>
      <div>
        <p>{{ currentUser.message }}</p>
        <button>상태메세지 변경하기</button>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'ProfileModify',
  computed: {
    currentUser () {
      return this.$store.getters.currentUser
    }
  }

}
</script>

<style>

</style>