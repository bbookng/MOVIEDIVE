<template>
  <div id="collection-detail" class="container"  v-if="collection">
    <CollectionDetailHeader :url="mainPosterURL"/>
    <CollectionDetailInfo :collection_pk="collection_pk" :currentUser="currentUser"/>
    <CollectionDetailMovies :collection="collection"/>
    <CollectionDetailComments :collection_pk="collection_pk"/>
  </div>
</template>

<script>
import axios from 'axios';
import CollectionDetailHeader from '@/components/collections/detail/CollectionDetailHeader.vue';
import CollectionDetailInfo from '@/components/collections/detail/CollectionDetailInfo.vue';
import CollectionDetailMovies from '@/components/collections/detail/CollectionDetailMovies.vue';
import CollectionDetailComments from '@/components/collections/detail/CollectionDetailComments.vue';

const API_URL = 'http://127.0.0.1:8000/api'

export default {
  name: "CollectionDetailView",
  components: {
    CollectionDetailHeader,
    CollectionDetailInfo,
    CollectionDetailMovies,
    CollectionDetailComments
  },
  data() {
    return {
      collection: null,
      mainPosterURL: null,
      suggest: null,
    };
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser
    },
    collection_pk() {
      return this.$route.params.collectionPk
    }
  },
  methods: {
    getCollection(collection_pk) {
      
      axios({
        url: `${API_URL}/collections/${collection_pk}/`,
        method: 'get',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        this.collection = res.data
        this.mainPosterURL = `https://image.tmdb.org/t/p/original/${res.data.movies[0].backdrop_path}`
      })
    },
  },
  created() {
    this.getCollection(this.collection_pk)
  },
  // destroyed() {
  //   this.$store.commit("SET_ISCOLLECTION_DETAIL", false);
  // },
};
</script>

<style>
#collection-detail {
  margin-top: 100px;
  width: 80vw;
  border: 1px solid black;
  padding: 0;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  background-color: whitesmoke;
}

</style>