<template>
  <div id="suggestions">
    <div v-for="suggest in suggests" :key="suggest.title">
        <div @click="select_suggestion(suggest.pk)">
            <img :src=imgURL(suggest.poster_path) alt="포스터입니당.">
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'MovieSuggestionList',
    props: {
        suggests: Array
    },
    computed: {
        imgURL(poster) {
            return `https://image.tmdb.org/t/p/original/${poster}`
        }
    },
    methods: {
        select_suggestion(pk){
            this.$emit('pkFromSuggestions', pk)
        }
    }
}
</script>

<style>

</style>