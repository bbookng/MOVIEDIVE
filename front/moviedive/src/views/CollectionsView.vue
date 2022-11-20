<template>
  <div id="collection-view-container" class="container">
    <CollectionList/>
  </div>
</template>

<script>
import CollectionList from "@/components/collections/CollectionList.vue";

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
  },
  computed: {
  },
  methods: {
    getCollections() {
      this.$store.dispatch("getCollections");
    },
  },
  created() {
    this.getCollections();
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