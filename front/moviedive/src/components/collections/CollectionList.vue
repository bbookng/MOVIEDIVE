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
import axios from 'axios';
import CollectionListItem from "@/components/collections/CollectionListItem.vue";
import CollectionCreationFrom from "@/components/collections/CollectionCreationForm.vue"

const API_URL = 'http://127.0.0.1:8000/api'

export default {
  name: "CollectionList",
  data() {
    return {
      create_collection: false,
      collections: null,
    }
  },
  components: {
    CollectionListItem,
    CollectionCreationFrom,
  },
  methods: {
    showCreationForm() {
      this.create_collection = true
    },
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