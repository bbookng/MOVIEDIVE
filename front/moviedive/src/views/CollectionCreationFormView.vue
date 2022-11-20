<template>
    <div>
      <form @submit.prevent="createCollection">
      <label for="collection_title">이름 : </label>
      <input type="text" id="collection_title" v-model="collection_title">
  
      <br>
  
      <label for="collection_description">설명 : </label>
      <input type="textarea" id="collection_description" v-model="collection_description">
  
      <br>
  
      <input type="submit" value="컬렉션 생성하기">
      </form>
  
  
      {{ selected_movies }}
  
  
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  const API_URL = 'http://127.0.0.1:8000/api'
  
  export default {
      name: 'CollectionCreationView',
      props: {
          selected_movies: Array,
          isSelected: Boolean,
      },
      data() {
          return {
              collection_title: '',
              collection_description: '',
          }
      },
      computed: {
          selected_movies_pk() {
              return this.selected_movies.map(movie => movie.pk)
          }
          
      },
      methods: {
          createCollection() {
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
                  this.$router.push({ name: 'collection' })
              })
              .catch((err) => {
                  console.log(err)
              })
      },
      }
  
  }
  </script>
  
  <style>
  
  </style>