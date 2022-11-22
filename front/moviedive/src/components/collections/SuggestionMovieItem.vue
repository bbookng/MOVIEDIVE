<template>
  <div>
    <img :src=imgURL alt="">
  </div>
</template>

<script>
export default {
    name: 'SuggestionMovieItem',
    props: {
        suggest: Object,
    },
    data() {
        return {
            imgURL: `https://image.tmdb.org/t/p/original/${this.suggest.poster_path}`
        }
    },

}
</script>

<style scope>
img {
    cursor: pointer;
    width: 100%;
    height: 100%;
}

</style>