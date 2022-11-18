<template>
  <div>
    <p>{{ collection.title }}</p>
    <img
      class="collectionPoster"
      :src="mainImgURL"
      alt="..."
      @click="showCollectionDetail"
    />
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
    showCollectionDetail() {
      this.$store.commit("SET_ISCOLLECTION_DETAIL", true),
      this.$emit('sendcollection', this.collection.pk)
    },
  },
};
</script>

<style>
.collectionPoster {
  cursor: pointer;
}
</style>