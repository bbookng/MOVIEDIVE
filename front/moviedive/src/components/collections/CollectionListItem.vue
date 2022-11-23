<template>
  <div>
    <div id="collection-item">
      <router-link style="text-decoration: none" :to="{ name: 'collection_detail', params: { collectionPk: this.collection.pk }}">
        <figure>
            <img
            class="collectionPoster"
            :src="mainImgURL"
            alt="..."
            />
            <figcaption>
              <div class="collection-description">
                <p class="my-2">좋아요 {{ collection.like_users_cnt }}  댓글 {{ collection.comments_cnt }}</p>   
              </div>
            </figcaption>
          </figure>
          <div class="collection-info">
            <h5 >{{ collection.title }}</h5>
            <router-link style="text-decoration: none; color: black;" class="comment-user" :to="{ name: 'mypage', params: { username: collection.user.username} }">
              <div id="collection-user" class="d-flex justify-content-start align-items-center">
                <img id="profile-img" :src=profileImg alt="">
                <p class="my-0 mx-1">{{ collection.user.nickname }}</p>
              </div>
            </router-link>
          </div>
      </router-link>
    </div>
  </div>
</template>

<script>

export default {
  name: "CollectionListItem",
  props: {
    collection: Object,
  },
  data() {
    // 메인 포스터는 뭐할지 나중에 수정
    return {
      mainImgURL: `https://image.tmdb.org/t/p/original/${this.collection.movies[0].poster_path}`,
    };
  },
  computed: {
    profileImg() {
      return this.collection.user.profile_img
    }
  },
  methods: {

  },
};
</script>

<style scoped>

.collectionPoster {
  cursor: pointer;
  border-radius: 7px;
}

#collection-item figure {
  width: 100%;
  height: 100%;
  position: relative;
}

#collection-item figcaption {
  width: 100%; height: 100%;
  background-color: rgba(0,0,0,0.7);

  position: absolute; /* 이미지와 겹치게 처리 */
  top: 0; left: 0;

  color: #fff; 
  text-align: left ;

  opacity: 0; /* 처음엔 안보이고 */

  transition: 0.3s;
  display:flex;
  align-items: flex-end;
}

#collection-item figcaption:hover , #collection-item figcaption:focus  {
  opacity: 1;
}

.collection-description {
  padding-top: 0px;
  padding-left: 10px;
  margin: 5px;
}

.collection-info {
  color: black;
  text-decoration: none;
}

#profile-img {
  border-radius: 50%;
  height: 60px;
  width: 60px;
  margin:0;
}
</style>