<template>
  <div>
    <CollectionListItem
      v-for="collection in collections"
      :key="collection.id"
      :collection="collection"
    />
    <p>?</p>
  </div>
</template>

<script>
import CollectionListItem from "@/components/collections/CollectionListItem.vue";

export default {
  name: "CollectionList",
  props: {},
  components: {
    CollectionListItem,
  },
  computed: {
    collections() {
      return this.$store.state.collections;
    },
  },
  methods: {},
};
</script>

<style>
</style>