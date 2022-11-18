<template>
  <div>
    <CollectionListItem
      v-for="collection in collections"
      :key="collection.id"
      :collection="collection"
      @click="getCollectionDetail"
      />
  </div>
</template>

<script>
import CollectionListItem from '@/components/collections/CollectionListItem.vue'
export default {
  name: 'CollectionList',
  components: {
    CollectionListItem,
  },
  computed: {
    collections() {
      return this.$store.state.collections
    }
  },
  methods: {
        getCollectionDetail() {
            this.$router.push({name: 'collection_detail', params: { pk: this.collection.user.pk}})
            
        }
    }



}
</script>

<style>

</style>