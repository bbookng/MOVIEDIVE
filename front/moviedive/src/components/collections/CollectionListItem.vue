<template>
  <div>
    <p>{{ collection.title }}</p>
    <img :src=mainImgURL alt="..." @click="getCollectionDetail">

  </div>
</template>

<script>
export default {
    name: 'CollectionListItem',
    props: {
        collection: Object
    },
    data() {
        return {
            mainImgURL: `https://image.tmdb.org/t/p/original/${ this.collection.movies[0].poster_path }`
        }
    },
    computed: {
    
    },
    methods: {
        getCollectionDetail() {
            
        }
    }

}
</script>

<style>

</style>