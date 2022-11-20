<template>
  <div>
    <div v-if="!create_collection">
      <button @click="showCreationForm">새 컬렉션</button>
      <CollectionListItem/>
      <hr>
      <CollectionListItem 
        v-for="collection in collections"
        :key="collection.id"
        :collection="collection"
      />
    </div>
    <CollectionCreationFrom v-if="create_collection"/>
  </div>
</template>

<script>
import CollectionListItem from "@/components/collections/CollectionListItem.vue";
import CollectionCreationFrom from "@/components/collections/CollectionCreationForm.vue"
export default {
  name: "CollectionList",
  data() {
    return {
      collection_pk: null,
      create_collection: false,
    }
  },
  props: {

  },
  components: {
    CollectionListItem,
    CollectionCreationFrom,
  },
  computed: {
    collections() {
      return this.$store.state.collections;
    },

  },
  methods: {
    showCreationForm() {
      this.create_collection = true
    }
  },
};
</script>

<style>
</style>