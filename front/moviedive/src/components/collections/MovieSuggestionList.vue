<template>
  <div>
    <div class="row">
        <div class="col-3 suggest-movies" @click="select_suggestion(suggest)" v-for="suggest in suggests" :key="suggest.pk" :suggest="suggest">
            <SuggestionMovieItem :selected_movies="selected_movies" :suggest="suggest"/>
        </div>
    </div>
  </div>
</template>

<script>
import SuggestionMovieItem from './SuggestionMovieItem.vue'

export default {
    name: 'MovieSuggestionList',
    components: {
        SuggestionMovieItem
    },
    data() {
        return {
            suggestList: [],
        }
    },
    props: {
        suggests: Array,
        selected_movies:Array,
    },
    computed: {
    },
    methods: {
        select_suggestion(suggest){
            this.$emit('FromSuggestions', suggest)
        }
    },
    created() {

    }
}
</script>

<style scoped>

.suggest-movies {
    width: 200px;
    height: 300px;
}

</style>