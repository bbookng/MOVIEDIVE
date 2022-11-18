<template>
  <div>
    <h1>Hello, Collections !</h1>
<<<<<<< HEAD
    <router-link :to="{ name:'create_collection' }">새 컬렉션</router-link>
    <CollectionList/>
=======
    <router-link :to="{ name: 'create_collection' }">새 컬렉션</router-link>
    <CollectionList v-if="!isCollectionDetail" />
    <CollectionDetail v-if="isCollectionDetail" />
>>>>>>> fb94408605ed4286aa388d9f9a2627d8ed6a9ef1
  </div>
</template>

<script>
import CollectionList from "@/components/collections/CollectionList.vue";
import CollectionDetail from "@/components/collections/CollectionDetail.vue";

export default {
  name: "CollectionsView",
  data() {
    return {
      isDetail: false,
    };
  },
  components: {
    CollectionList,
    CollectionDetail,
  },
  computed: {
    isCollectionDetail() {
      return this.$store.state.isCollectionDetail;
    },
  },
  methods: {
    getCollections() {
      this.$store.dispatch("getCollections");
    },
    createCollection() {},
  },
  created() {
    this.getCollections();
  },
};
</script>

<style>
</style>