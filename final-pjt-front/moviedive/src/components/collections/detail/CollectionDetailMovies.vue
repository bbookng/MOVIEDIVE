<template>
    <div id="collection-detail-movies">
      <h3 id="collection-movies">작품들</h3>
      <div div="container">
        <div class="row">
          <div class="col-3" v-for=" movie in collection.movies" :key="movie.pk" >
            <div>
              <CollectionMovieItem :movie="movie"/>
              <p style="padding-left: 15px;">{{ movie.title }}</p>
            </div>
          </div>
        </div>
      </div>  
    </div>
  </template>
  
  <script>
  import CollectionMovieItem from '@/components/collections/CollectionMovieItem'
  export default {
      name: "CollectionDetailMovies",
      props: {
        collection: Object,
      },
      components: {
        CollectionMovieItem,
    }
  }
  </script>
  
  <style>
  #collection-detail-movies{
    margin-left: 15%;
    margin-right: 15%;
    text-align: left;
  }

  #collection-movies {
    padding-top: 1rem;
    padding-left: 1rem;
  }

  </style>