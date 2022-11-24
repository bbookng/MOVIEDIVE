<template>
    <div id="collection-create-form">
        <div v-if="!isSelected">
            <div>
                <div v-if="selected_movies.length > 0" style="padding: 2rem; width: 300px;">
                    <p class="mx-0">현재 담긴 영화들</p>
                    <div>
                        <SuggestionMovieItem v-for="suggest in selected_movies" :key="suggest.pk" :suggest="suggest"/>
                    </div>
                </div>
                <div id="select-form-movies">
                    <h5>당신의 컬렉션을 만들어보세요 !</h5>
                    <input autocomplete="off" @input="getSuggestions" :search_keyword="search_keyword" type="text" id="nc-search-keyword" placeholder="  영화제목을 입력해주세요." />
                </div>
                    <button v-if="selected_movies.length > 0" @click="createCollection">선택완료</button>
            </div>
            <div class="container">
                <MovieSuggestionList :selected_movies="selected_movies" @FromSuggestions="selectMovie" :suggests="suggests"/>
            </div>
        </div>
        <div id="collection-complete-box" v-if="isSelected" >
            <h5>당신의 컬렉션을 만들어보세요 !</h5>
            <form id="collection-input-box" @submit.prevent="saveCollection">
                <div id="collection-title-box">
                    <label for="collection_title">title : </label>   
                    <input type="text" id="collection_title" v-model="collection_title">
                </div>
                <div id="collection-description-box">
                    <label for="collection_description">description : </label>
                    <input type="textarea" id="collection_description" v-model="collection_description">
                </div>
                <button @click="selectMovies">영화 선택하기</button>
                <input type="submit" value="컬렉션 만들기">
                <div class="container">
                    <div class="row">
                        <SuggestionMovieItem class="col-4" v-for="suggest in selected_movies" :key="suggest.pk" :suggest="suggest"/>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import SuggestionMovieItem from '@/components/collections/SuggestionMovieItem'
import MovieSuggestionList from "@/components/collections/MovieSuggestionList.vue"
import axios  from "axios"

const API_URL = 'http://127.0.0.1:8000/api'

export default {
    name: 'CollectionCreationForm',
    components:{
        MovieSuggestionList,
        SuggestionMovieItem
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
            return this.selected_movies.map(movie => movie.pk)
          },
    },
    created() {
        this.getCollection()
    },
    methods: {
        selectMovie(suggest) {
            // 포함되어 있으면 제거하고 없으면 들어가게 로직 다시 짜기
            console.log(suggest)
            if (this.selected_movies.includes(suggest)) {
                console.log("a")
                let why = this.selected_movies.filter((sm) => {
                    console.log(parseInt(sm.pk) != parseInt(suggest.pk))
                    return parseInt(sm.pk) != parseInt(suggest.pk)})
                
                this.selected_movies = why
            } else {
                this.selected_movies = [...this.selected_movies, suggest]
            }
            
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
            if (this.selected_movies.length == 0) {
                alert('영화를 선택해주세요.')
            } else {
                this.isSelected = true
            }
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
#collection-create-form {
    margin-left: 15%;
    margin-right: 15%;
}

label {
    width: 100px;
}

#collection-input-box {
    text-align: left;
}

#collection-title-box {
    margin-bottom: 10px;
}

#collection-description-box {
    margin-bottom: 10px;
}

#collection-complete-box {
    padding: 2rem;
}
#select-form-movies {
    margin-top: 15px;

}
#collection-title {
    width: 50%;
    border: solid 1px rgba(0, 0, 0, 0.63);
    border-radius: 5px;
}
#collection_description {
    width: 50%;
    height: 6.25em;
    border: solid 1px rgba(0, 0, 0, 0.63);
    border-radius: 5px;
    resize: none;
  }

#nc-search-keyword {
    width: 35rem;
    height: 2.5rem;
    border-radius: 5px;
    margin-bottom: 15px;
}

</style>