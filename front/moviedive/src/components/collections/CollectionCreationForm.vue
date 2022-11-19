<template>
    <div>
    <div v-if="!isSelected">
        <div>
            <h4>컬렉션 만들기</h4>
            <h5>영화들을 골라주세요</h5>
            <input autocomplete="off" @input="getSuggestions" :search_keyword="search_keyword" type="text" id="nc-search-keyword" placeholder="영화제목을 입력해주세요" />
        </div>
        <button @click="createCollection">선택완료</button>
        <div v-if="selected_movies">
            <span>
                {{ selected_movies }}
            </span>
        </div>
        <div>
            <MovieSuggestionList selected_movies="selected_movies" @FromSuggestions="selectMovie" :suggests="suggests"/>
        </div>
    </div>
    <div v-if="isSelected">
        <CollectionCreate
          :selected_movies="selected_movies"
          :isSelected="isSelected"
        />
    </div>
    </div>
</template>

<script>
import MovieSuggestionList from "@/components/collections/MovieSuggestionList.vue"
import CollectionCreate from '@/components/collections/CollectionCreate.vue'
import axios  from "axios"

export default {
    name: 'CollectionCreationForm',
    components:{
        MovieSuggestionList,
        CollectionCreate,
    },
    data() {
        return {
            search_keyword: "",
            suggests: null,
            selected_movies: [],
            isSelected: false,
            select_movie: null,
        }
    },
    computed: {
        
    },
    methods: {
        selectMovie(suggest) {
            this.selected_movies = [...this.selected_movies, suggest]
        },
        getSuggestions(event){
            const API_URL = 'http://127.0.0.1:8000/api/'

            axios({
                method: 'get',
                url: API_URL + `collections/create/suggest/${event.target.value}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
            })
            .then((res) => {
                this.suggests = res.data
            })
        },
        createCollection() {
            this.isSelected = true
        }
    }
}
</script>

<style>

</style>