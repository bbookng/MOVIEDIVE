<template>
  <div>
    <div>
        <div @click="select_suggestion(suggest)" v-for="suggest in suggests" :key="suggest.pk" :suggest="suggest">
            <SuggestionMovieItem :suggest="suggest"/>
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
            suggest: [],
        }
    },
    props: {
        suggests: Array
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

<style>

</style>