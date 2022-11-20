<template>
  <div>
    <p>{{ collection.title }}</p>
    <router-link :to="{ name: 'collection_detail', params: { collectionPk: this.collection.pk }}">
      <img
      class="collectionPoster"
      :src="mainImgURL"
      alt="..."
      />
    </router-link>
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
  computed: {},
  methods: {

  },
};
</script>

<style>
.collectionPoster {
  cursor: pointer;
}
</style>