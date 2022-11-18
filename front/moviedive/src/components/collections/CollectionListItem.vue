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
        // 메인 포스터는 뭐할지 나중에 수정
        return {
            mainImgURL: `https://image.tmdb.org/t/p/original/${ this.collection.movies[0].poster_path }`
        }
    },
    computed: {
    
    },
    methods: {
        getCollectionDetail() {
            this.$route.push({name: 'collection_detail', params: { pk: this.collection.user.pk}})
            
        }
    }

}
</script>

<style>

</style>