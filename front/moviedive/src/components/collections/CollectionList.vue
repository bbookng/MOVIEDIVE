<template>
  <div>
    <div>
      <router-link id="new-collection" :to="{ name: 'save_collection' }">+ 컬렉션 만들기</router-link>
      <div class="container" id="user-like-collections">
        <h3>{{ currentUser.nickname }}님이 좋아요한 컬렉션</h3>
        <div class="row">
          <CollectionListItem
          class="col-3"
          v-for="collection in userlikecollections"
          :key="collection.id"
          :collection="collection"
          />
        </div>
      </div>
      <hr>
      <div class="container">
        <h3>이런 컬렉션은 어떠세요 ?</h3>
        <div class="row">
          <CollectionListItem 
          class="col-3"
          v-for="collection in collections"
          :key="collection.id"
          :collection="collection"
          />
        </div>
      </div>
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
          console.log(res.data)
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
#new-collection {
  text-decoration: none;
  position: absolute;
  left: 150px;
  margin-top: 1rem;
  font-size: large;
  color: white;
}

.h3 {
  color: rgb(250, 251, 252);
}

</style>