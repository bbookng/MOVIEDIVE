<template>
    <div id="collection-create-form">
        <div v-if="!isSelected">
            <div v-if="selected_movies.length > 0" id="selected-movies-list">
                <h5 style="font-weight: 600;">
                    <img id="camera-icon" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/camera.png" alt="">
                    현재 담긴 영화들
                </h5>
                <div class="container">
                    <div class="row">
                        <div  class="col-2" v-for="suggest in selected_movies" :key="suggest.pk">
                            <SuggestionMovieItem  :suggest="suggest"/>
                        </div>
                    </div>
                </div>
            </div>
            <button class="btn btn-outline-dark" v-if="selected_movies.length > 0" @click="createCollection">선택완료 !</button>
            <div id="select-form-movies">
                <input autocomplete="off" @input="getSuggestions" :search_keyword="search_keyword" type="text" id="nc-search-keyword" placeholder="   컬렉션에 담을 영화 제목을 입력해주세요." />
            </div>
            <div class="movie-suggestion-list" style="padding:5px;">
                <MovieSuggestionList :selected_movies="selected_movies" @FromSuggestions="selectMovie" :suggests="suggests"/>
            </div>
        </div>
        <div id="collection-complete-box" v-if="isSelected" >
            <form id="collection-input-box" @submit.prevent="saveCollection">
                <div id="collection-title-description-box">
                    <div id="collection-title-box">
                        <label for="collection_title">title : </label>   
                        <input type="text" id="collection-title" v-model="collection_title" placeholder="   컬렉션 제목을 입력해주세요.">
                    </div>
                    <div id="collection-description-box">
                        <label for="collection_description">description : </label>
                        <input type="textarea" id="collection_description" v-model="collection_description" placeholder="   컬렉션 설명을 입력해주세요.">
                    </div>
                </div>
                <div class="d-flex justify-content-center">
                    <button class="collection-create-button" @click="selectMovies">영화 선택하기</button>
                    <input class="collection-create-button" type="submit" value="컬렉션 만들기">
                </div>
                <div class="container">
                <div class="row">
                    <div class="col-2" v-for="suggest in selected_movies" :key="suggest.pk">
                        <SuggestionMovieItem  :suggest="suggest"/>
                    </div>                        
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

const API_URL = 'https://moviedive.co.kr/api'

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
            return this.selected_movies.map((movie) => {
                if (movie.pk) {
                    return movie.pk
                }else {
                    return movie.id;
                }});
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
            const API_URL = 'https://moviedive.co.kr/api/'

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

/* .select-complete-button {
    background: none;
    border: 1px solid black;
    border-radius: 5%;
} */

#collection-title-description-box{
    text-align: center;
}
#selected-movies-list {
    padding: 2rem;
    text-align: left;
}

#camera-icon {
    width: 50px;
    height: 50px;
    margin-bottom: 2px;
    text-align: center;

}
#collection-create-form {
    margin-left: 15%;
    margin-right: 15%;
    border-left: 1px solid gray;
    border-right: 1px solid gray;
    background-color: white;
    height: 1200px;
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

#collection-title {
    width: 500px;
    border: solid 1px rgba(0, 0, 0, 0.63);
    border-radius: 5px;
    resize: none;
}
#collection_description {
    width: 500px;
    height: 6.25em;
    border: solid 1px rgba(0, 0, 0, 0.63);
    border-radius: 5px;
    resize: none;
  }

#nc-search-keyword {
    width: 35rem;
    height: 3rem;
    border-radius: 20px;
    margin-bottom: 15px;
    margin: 2rem;

}

.collection-create-button {
    height: 30px;
    border: solid 1px gray;
    border-radius: 20px;
    background-color: transparent;
    margin: 1rem;
}
</style>