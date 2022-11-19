<template>
  <div>
    <div v-if="!create_collection">
      <button @click="showCreationForm">새 컬렉션</button>
      <CollectionListItem 
        v-for="collection in collections"
        :key="collection.id"
        :collection="collection"
        @sendcollection="sendCollection"
      />
    </div>
    <CollectionCreationFrom v-if="create_collection"/>
    <p>?</p>
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
    sendCollection(collection_pk) {
      this.collection_pk = collection_pk
      this.$emit('sendcollection', this.collection_pk)
      console.log(this.collection_pk)
    }, 
    showCreationForm() {
      console.log(1)
      this.create_collection = true
    }
  },
};
</script>

<style>
</style>