<template>
  <div>
    <div v-if="!create_collection">
      <router-link :to="{ name: 'save_collection' }">새 컬렉션</router-link>
      <div>
        <h3>{{ currentUser.nickname }}님이 좋아요한 컬렉션</h3>
        <CollectionListItem
        v-for="collection in userlikecollections"
        :key="collection.id"
        :collection="collection"
        />
      </div>
      <hr>
      <h3>이런 컬렉션은 어떠세요 ?</h3>
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
      userlikecollections: null,
    }
  },
  components: {
    CollectionListItem,
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser
    }
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
    getUserLikeCollections() {
      axios({
          url: `${API_URL}/collections/${this.currentUser.username}/likes`,
          method: 'get',
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res)=>{
          console.log(res.data)
          this.userlikecollections = res.data.like_collections
        
        })

    }
  },
  created() {
    this.getCollections();
    this.getUserLikeCollections();
  },
};
</script>

<style>
</style>