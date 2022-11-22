<template>
  <div id="my-page-header" class="container">
    <div class="row">
      <div class="col-4 d-flex justify-content-end">
        <div id="profile-img-box">
          <img
            id="profile-img"
            src="https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F83%2F1f%2Fda%2F831fdaa1b75381f6ff74de37de6e938d.jpg&type=sc960_832"
            alt="프로필 이미지"
          />
        </div>
      </div>
      <div class="col-8 d-flex align-items-end">
        <div
          id="profile-informations"
          class="d-flex flex-column justify-content-end align-items-start"
        >
          <div class="d-flex align-items-center">
            <div>{{ user.nickname }}</div>
            <button id="follow-button" class="mx-3">팔로우</button>
          </div>
          <div class="my-2">
            리뷰 {{ user.reviews_cnt }} | 팔로워 {{ user.followers_cnt }} |
            팔로잉 {{ user.followings_cnt }}
          </div>
          <div class="status">상태 메시지</div>
        </div>
      </div>
    </div>
    <div id="highlights" class="row">하이라이트 컬렉션 들어갈 자리</div>
  </div>
</template>

<script>
export default {
  name: "MyPageHeader",
  props: {
    profileImg: String,
    user: Object,
  },
};
</script>

<style>
#my-page-header {
  height: 470px;
}
#profile-img {
  margin-top: 8vh;
  border-radius: 50%;
  border: white 3px solid;
  height: 170px;
  width: 170px;
}
#follow-button {
  background-color: white;
  border: black 1px solid;
  border-radius: 4px;
}
#profile-informations {
  padding-bottom: 40px;
  padding-left: 15px;
}
#highlights {
  border: 1px black solid;
  margin-top: 20px;
  padding-left: 60px;
}
</style>