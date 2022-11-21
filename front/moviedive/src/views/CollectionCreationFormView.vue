<template>
    <div>
    <div v-if="!isselectCollection">

        <form @submit.prevent="saveCollection">
            <label for="collection_title">이름 : </label>   
            <input type="text" id="collection_title" v-model="collection_title">
            
            <br>
            <label for="collection_description">설명 : </label>
            <input type="textarea" id="collection_description" v-model="collection_description">
            
            <br>
            <button @click="selectMovies">영화 선택하기</button>
            <input type="submit" value="컬렉션 생성하기">
        </form>
        
    </div>

    <CollectionCreationForm
       v-if="isselectCollection"
      :selected_movies="selected_movies"
      :isselectCollection="isselectCollection"
      @isselectCollection="selectMovies"/>
  
      {{ selected_movies }}
      {{ collection_movies }}
  
  
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import CollectionCreationForm from '@/components/collections/CollectionCreationForm.vue'

  const API_URL = 'http://127.0.0.1:8000/api'
  
  
  export default {
      name: 'CollectionCreationFormView',
      components: {
        CollectionCreationForm
      },
      data() {
          return {
              collection_title: '',
              collection_description: '',
              collection_pk: this.$route.params.collectionPk,
              collection_movies: null,
              isselectCollection: false,
          }
      },
      computed: {
          selected_movies() {
            return this.$store.getters.selected_movies
          },
          selected_movies_pk() {
            if (this.selected_movies) {
                return this.selected_movies.map(movie => movie.pk)
            } else {
                return false
            }
          },
      },
      mounted() {
        this.getCollection()
        this.selectMovies()
      },
      methods: {
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
                    this.collection_movies = res.data.movies
                    this.collection_title = res.data.title
                    this.collection_description = res.data.description
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
                    url: `${API_URL}/collectinons/${this.collection_pk}/`,
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
                    console.log(res)
                    alert('수정되었습니다.')
                    this.$router.push({ name: 'collection' })
                })
                .catch((err) => {
                    console.log(err)
                })
            }
        },
        selectMovies() {
            this.isselectCollection = !this.isselectCollection
        }
    }
  
  }
  </script>
  
  <style>
  
  </style>