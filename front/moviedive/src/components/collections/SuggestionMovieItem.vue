<template>
  <div id="suggest-img">
    <img v-if="isSelected" style="opacity: 0.5;" :src=imgURL alt="">
    <img v-if="!isSelected" :src=imgURL alt="">
  </div>
</template>

<script>
export default {
    name: 'SuggestionMovieItem',
    props: {
        suggest: Object,
        selected_movies:Array,
    },
    data() {
        return {
            imgURL: `https://image.tmdb.org/t/p/original/${this.suggest.poster_path}`
        }
    },
    computed: {
        isSelected() {
            return this.selected_movies.includes(this.suggest)
        }
    }

}
</script>

<style scope>
img {
    cursor: pointer;
    width: 100%;
    height: 100%;
    padding: 10px;
}
#suggest-img {
    width: 200px;
    height: 300px;
}

</style>