<template>
  <div>
    <div>
        <h4>컬렉션 만들기</h4>
        <h5>영화들을 골라주세요</h5>
        <input autocomplete="off" @input="getSuggestions" :value="search_keyword" type="search" id="nc-search-keyword" placeholder="영화제목을 입력해주세요" />
    </div>
    <div>
        <MovieSuggestionList id="suggestion-box" :selected_movies="selected_movies" @pkFromSuggestion="selectMovie" :suggests="suggests"></MovieSuggestionList>
    </div>
  </div>
</template>

<script>
import MovieSuggestionList from "@/components/collections/MovieSuggestionList.vue"
export default {
    name: 'CollectionCreationForm',
    components:{
        MovieSuggestionList
    },
    data() {
        return {
            search_keyword: "",
            suggests: [],
            selected_movies: []
            
        }
    },
    methods: {
        changeKeyword(event) {
            this.search_keyword = event.target.value
            this.autoComplete(this.search_keyword)
        },
        selectMovie(pk) {
            this.selected_movies = [...this.selected_movies, pk]
        },
        getSuggestions(){
            axios({
                method: 'get',
                url: 
            })
        }
    }
}
</script>

<style>

</style>