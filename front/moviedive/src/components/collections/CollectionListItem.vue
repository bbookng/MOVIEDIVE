<template>
  <div>
    <!-- <p>{{ collection.title }}</p> -->
    <router-link :to="{ name: 'collection_detail', params: { collectionPk: this.collection.pk }}">
      <img
      class="collectionPoster"
      :src="mainImgURL"
      alt="..."
      />
    </router-link>
    {{ collection.like_users_cnt }}
    {{ collection.comments_cnt }}
    <div id="selectcollection">
      {{ collection.title }}
      {{ collection.description }}
      <div>
        <img :src=profileImg alt="프로필이미지">
        {{ collection.user.nickname }}
      </div>
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
      return this.collection.profile_img
    }
  },
  methods: {

  },
};
</script>

<style>
.collectionPoster {
  cursor: pointer;
}
</style>