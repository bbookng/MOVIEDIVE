<template>
  <div class="d-flex align-items-center">
    <img class="profile-thumbnail" :src="user.profile_img" alt="프로필 사진" />
    <p class="profile-nickname">{{ user.nickname }}</p>
  </div>
</template>

<script>
export default {
  name: "ConnectedUser",
  props: {
    user: Object,
  },
};
</script>

<style>
.profile-thumbnail {
  width: 25px;
  height: 25px;
  border-radius: 50%;
  margin: 5px;
  margin-left: 12px;
}
.profile-nickname {
  margin: 5px;
}
</style>