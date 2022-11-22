<template>
  <div>
    <div>
        <div class="container" @click="select_suggestion(suggest)" v-for="suggest in suggests" :key="suggest.pk" :suggest="suggest">
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
            console.log(suggest)
            this.$emit('FromSuggestions', suggest)
        }
    },
    created() {

    }
}
</script>

<style scoped>
.container {
    display: grid;
    grid-template-columns: 300px, 300px, 300px, 300px;
}


</style>