<template>
    <div>
    <div v-if="!isSelected">
        <div>
            <h4>컬렉션 만들기</h4>
            <h5>영화들을 골라주세요</h5>
            <input autocomplete="off" @input="getSuggestions" :search_keyword="search_keyword" type="text" id="nc-search-keyword" placeholder="영화제목을 입력해주세요" />
        </div>
        <button @click="createCollection">선택완료</button>
        <div class="container">
            <MovieSuggestionList :selected_movies="selected_movies" @FromSuggestions="selectMovie" :suggests="suggests"/>
        </div>
        {{ selected_movies }}
    </div>
    <div v-if="isSelected">
        <form @submit.prevent="saveCollection">
            <label for="collection_title">이름 : </label>   
            <input type="text" id="collection_title" v-model="collection_title">
            
            <br>
            <label for="collection_description">설명 : </label>
            <input type="textarea" id="collection_description" v-model="collection_description">
            
            <br>
            <button @click="selectMovies">영화 선택하기</button>
            <input type="submit" value="컬렉션 만들기">
            {{ selected_movies }}
        </form>
    </div>
    </div>
</template>

<script>
import MovieSuggestionList from "@/components/collections/MovieSuggestionList.vue"
import axios  from "axios"

const API_URL = 'http://127.0.0.1:8000/api'

export default {
    name: 'CollectionCreationForm',
    components:{
        MovieSuggestionList,
    },
    data() {
        return {
            search_keyword: "",
            suggests: null,
            selected_movies: [],
            isSelected: false,
            selectd_movie: null,
            collection_title: '',
            collection_description: '',
            collection_pk: this.$route.params.collectionPk,
            collection_movies: null,
        }
    },
    computed: {
        selected_movies_pk() {
            return this.selected_movies.map(movie => movie.id)
          },
    },
    mounted() {
        this.getCollection()
    },
    methods: {
        selectMovie(suggest) {
            // 포함되어 있으면 제거하고 없으면 들어가게 로직 다시 짜기
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
        },
        getCollection() {
            if (this.collection_pk !== undefined) {
                axios({
                    method: 'get',
                    url: `${API_URL}/collections/${this.collection_pk}/`,
                    headers: {
                    Authorization: `Token ${this.$store.state.token}`
                    } 
                })
                .then((res) => {
                    this.selected_movies = res.data.movies
                    this.collection_title = res.data.title
                    this.collection_description = res.data.description
                    this.isSelected = true
                })
                .catch((err) => {
                    console.log(err)
                })
            }

        },
        saveCollection() {
            const title = this.collection_title
            const description = this.collection_description
            
            if (!title) {
                alert('제목을 입력해주세요')
            } else if (!description) {
                alert ('내용을 입력해주세요')
            }
            if (this.collection_pk === undefined) {

                axios({
                    method: 'post',
                    url: `${API_URL}/collections/create/`,
                    headers: {
                        Authorization: `Token ${this.$store.state.token}`
                    },
                    data: {
                        movies: this.selected_movies_pk,
                        title: this.collection_title,
                        description: this.collection_description,
                    }
                })
                .then((res) => {
                    console.log(res.data)
                    alert('컬렉션 생성 완료!')
                    this.$router.push({ name: 'collection' })
                })
                .catch((err) => {
                    console.log(err)
                })
            } else {
                axios({
                    method: 'put',
                    url: `${API_URL}/collections/${this.collection_pk}/`,
                    headers: {
                        Authorization: `Token ${this.$store.state.token}`
                    },
                    data: {
                        movies: this.selected_movies_pk,
                        title: this.collection_title,
                        description: this.collection_description,
                    }
                })
                .then((res) => {
                    console.log(this.selected_movies_pk)
                    
                    console.log(res)
                    alert('수정되었습니다.')
                    this.$router.push({ name: 'collection' })
                })
                .catch((err) => {
                    console.log(this.selected_movies_pk)
                    console.log(err)
                })
            }
        },
        selectMovies() {
            this.isSelected = false
        }
    }
}
</script>

<style scoped>


</style>