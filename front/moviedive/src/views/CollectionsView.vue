<template>
  <div>
    <h1>Hello, Collections !</h1>
    <router-link :to="{name:'create_collection'}">새 컬렉션</router-link>
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