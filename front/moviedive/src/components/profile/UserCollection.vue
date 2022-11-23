<template>
  <div class="container">
    <div class="row">
      <CollectionListItem
        class="col-4"
        v-for="collection in collections"
        :key="collection.pk"
        :collection="collection" />
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import CollectionListItem from '../collections/CollectionListItem.vue';

export default {
    name: 'UserCollection',
    components: {
      CollectionListItem,
    },
    data() {
      return {
        collections: null,
      }
    },
    props: {
      user: Object,
    },
    methods: {
      getCollections(username) {
        axios({
          method: 'get',
          url: this.$store.state.API_URL + `/accounts/profile/${username}/collections/`,
          headers: this.$store.getters.authHeader
        })
        .then((res) => {
          console.log(res.data)
          this.collections = res.data.collections
        })
      }
    },
    created() {
      this.getCollections(this.user.username)
    }


}
</script>

<style scoped>
/* .container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-auto-rows: minmax(100px, auto);
  column-gap: 20px;
}
 */


</style>