<template>
    <div>
    <div>
        <div>
            <h4>컬렉션 만들기</h4>
            <h5>영화들을 골라주세요</h5>
            <input autocomplete="off" @input="getSuggestions" :search_keyword="search_keyword" type="text" id="nc-search-keyword" placeholder="영화제목을 입력해주세요" />
        </div>
        <button @click="createCollection">선택완료</button>
        <div>
            <MovieSuggestionList :selecte_movies="selecte_movies" @FromSuggestions="selectMovie" :suggests="suggests"/>
        </div>
        {{ selecte_movies }}
    </div>
    </div>
</template>

<script>
import MovieSuggestionList from "@/components/collections/MovieSuggestionList.vue"
import axios  from "axios"

export default {
    name: 'CollectionCreationForm',
    components:{
        MovieSuggestionList,
    },
    props: {
        selected_movies: Array,
        isselectCollection: Boolean,
    },
    data() {
        return {
            search_keyword: "",
            suggests: null,
            selecte_movies: [],
            isSelected: false,
            select_movie: null,
        }
    },
    computed: {
        isSelecteCollection() {
            return !this.isselectCollection
        }
        
    },
    created() {
        this.checkupdate()

    },
    methods: {
        checkupdate() {
            if (this.selected_movies) {
                this.selecte_movies = this.selected_movies
            }
        }
        ,
        selectMovie(suggest) {
            // 포함되어 있으면 제거하고 없으면 들어가게 로직 다시 짜기
            this.selecte_movies = [...this.selecte_movies, suggest]
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
            this.$store.commit('SET_COLLECTION', this.select_movies)
            this.isSelectCollection = false
            this.$emit('isselectCollection', this.isSelectCollection)
        }
    }
}
</script>

<style>

</style>