<template>
  <div>
    <label for="collection_title">이름 : </label>
    <input type="text" id="collection_title" v-model="collection_title">

    <br>

    <label for="collection_description">설명 : </label>
    <input type="textarea" id="collection_description" v-model="collection_description">

    <br>

    <button @click="createCollection">컬렉션 생성하기</button>


    {{ selected_movies }}


  </div>
</template>

<script>
export default {
    name: 'CollectionCreate',
    props: {
        selected_movies: Array,
    },
    data() {
        return {
            collection_title: '',
            collection_description: '',
        }
    },
    computed: {
        selected_movies_pk() {
            return this.selected_movies.map(movie => movie.pk)
        }
        

    },
    methods: {
        createCollection() {
            const collection_title = this.collection_title
            const collection_description = this.collection_description
            const selected_movies_pk = this.selected_movies_pk

            const payload = {
                collection_title,
                collection_description,
                selected_movies_pk
                }

            this.$store.dispatch('createCollection', payload)
        }
    }

}
</script>

<style>

</style>