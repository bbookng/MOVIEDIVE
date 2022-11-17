<template>
  <div>
    <CollectionListItem
      v-for="collection in collections"
      :key="collection.id"
      :collection="collection"
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
  }


}
</script>

<style>

</style>