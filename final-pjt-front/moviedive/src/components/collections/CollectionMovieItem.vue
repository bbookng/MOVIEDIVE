<template>
    <div id="suggest-img">
      <img id="suggets-img-item" :src=imgURL alt="">
    </div>
  </template>
  
  <script>
  export default {
      name: 'CollectionMovieItem',
      props: {
          movie: Object,
      },
      data() {
          return {
              imgURL: `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
          }
      },
  
  }
  </script>
  
  <style scope>
  #suggets-img-item {
      cursor: pointer;
      width: 100%;
      height: 100%;
      padding: 10px;
  }
  
  #suggest-img {
      width: 200px;
      height: 300px;
  }
  
  </style>