<template>
  <div>
    <h1>Hello, Collections !</h1>
    <button @click="createCollection">Create Collection</button>
    <CollectionList/>
  </div>
</template>

<script>
import CollectionList from '@/components/collections/CollectionList.vue'


export default {
  name: 'CollectionsView',
  data() {
    return {

    }
  },
  components: {
    CollectionList

  },
  methods: {
    getCollections() {
      this.$store.dispatch('getCollections')
    },
    createCollection() {
      
    }

  },
  created() {
    this.getCollections()
  }
}
</script>

<style>

</style>