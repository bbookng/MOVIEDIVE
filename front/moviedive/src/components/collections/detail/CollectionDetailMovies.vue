<template>
    <div id="collection-detail-movies">
      <h3>작품들</h3>  
      <div class="container">
        
        <div class="row" v-for=" suggest in collection.movies" :key="suggest.pk" >
        <SuggestionMovieItem class="col-3" :suggest="suggest"/>
        {{ suggest.title }}

        </div>
      </div>
    </div>
  </template>
  
  <script>
  import SuggestionMovieItem from '@/components/collections/SuggestionMovieItem'
  export default {
      name: "CollectionDetailMovies",
      props: {
        collection: Object,
      },
      components: {
        SuggestionMovieItem,
    }
  }
  </script>
  
  <style>
  #collection-detail-movies{
    border: solid black 1px;
    margin-left: 15%;
    margin-right: 15%;
  }
  </style>