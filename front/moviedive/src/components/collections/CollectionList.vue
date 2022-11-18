<template>
  <div>
    <CollectionListItem
      v-for="collection in collections"
      :key="collection.id"
      :collection="collection"
      @sendcollection="sendCollection"
    />
    <p>?</p>
  </div>
</template>

<script>
import CollectionListItem from "@/components/collections/CollectionListItem.vue";

export default {
  name: "CollectionList",
  data() {
    return {
      collection_pk: null,
    }

  },
  props: {

  },
  components: {
    CollectionListItem,
  },
  computed: {
    collections() {
      return this.$store.state.collections;
    },
  },
  methods: {
    sendCollection(collection_pk) {
      this.collection_pk = collection_pk
      this.$emit('sendcollection', this.collection_pk)
      console.log(this.collection_pk)
    }
  },
};
</script>

<style>
</style>