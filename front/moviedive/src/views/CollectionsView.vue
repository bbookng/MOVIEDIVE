<template>
  <div id="collection-view-container" class="container">
    <CollectionList @sendcollection="getCollection" v-if="!isCollectionDetail" />
    <CollectionDetail :collection_pk="collection_pk" v-if="isCollectionDetail" />
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
      collection_pk: null,
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
    getCollection(collection_pk) {
      this.collection_pk = collection_pk
      console.log(this.collection_pk)
    }
  },
  created() {
    this.getCollections();
    this.$store.commit("SET_ISCOLLECTION_DETAIL", false);
  },
};
</script>

<style>
#collection-view-container{
width: 100vw;
border-radius: 10px;
border: black 1px solid;
padding-left: 0;
padding-right: 0;
}
</style>