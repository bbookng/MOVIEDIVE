<template>
  <div id="collection-list" v-if="collections">
    <div>
      <div id="new-collection">
        <router-link id="new-collection" :to="{ name: 'save_collection' }">+ 컬렉션 만들기</router-link>
      </div>
      <div class="collection-list-title" id="user-like-collections">
        <div class="collection-list-kind">
          <p>{{ currentUser.nickname }}님이 좋아요한 컬렉션</p>
        </div>
        <div class="container">
          <div class="row">
            <CollectionListItem
            class="col-3"
            v-for="collection in userlikecollections"
            :key="collection.id"
            :collection="collection"
            />
          </div>
        </div>
      </div>
      <hr>
      <div class="collection-list-title">
        <div class="collection-list-kind">
          <p>이런 컬렉션은 어떠세요 ?</p>
        </div>
        <div class="container">
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

<style scoped>
#collection-list {
  margin-top: 20px;
  padding-left: 10%;
  padding-right: 10%;
}

#new-collection {
  text-decoration: none;
  text-align: right;
  font-size: large;
  margin-bottom: 10px;
  color: rgb(19, 1, 1);
  font-weight: bold;
  margin-right: 1rem;
}

.collection-list-kind{
  margin: 20px;
  font-style: normal;
  font-weight: 500;
  font-size: 35px;
  line-height: 51px;
}

.collection-list-title {
  text-align: left;
}

</style>