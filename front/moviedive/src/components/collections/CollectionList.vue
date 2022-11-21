<template>
  <div>
    <div v-if="!create_collection">
      <router-link :to="{ name: 'save_collection' }">새 컬렉션</router-link>
      <CollectionListItem/>
      <hr>
      <CollectionListItem 
        v-for="collection in collections"
        :key="collection.id"
        :collection="collection"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import CollectionListItem from "@/components/collections/CollectionListItem.vue";

const API_URL = 'http://127.0.0.1:8000/api'

export default {
  name: "CollectionList",
  data() {
    return {
      collections: null,
    }
  },
  components: {
    CollectionListItem,
  },
  methods: {
    getCollections() {
      axios({
          url: `${API_URL}/collections/`,
          method: 'get',
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res)=>{
          this.collections = res.data
        })
    },
  },
  created() {
    this.getCollections();
  },
};
</script>

<style>
</style>