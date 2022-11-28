<template>
  <div id="suggest-img">
      <figure>
        <img class="suggested-img" v-if="isSelected" style="opacity: 0.5;" :src=imgURL alt="">
        <img class="suggested-img" v-if="!isSelected" :src=imgURL alt="">
        <figcaption>
            <div class="suggested-title">
                <p>{{ suggest.title }}</p>
            </div>
        </figcaption>
    </figure>
  </div>
</template>

<script>
export default {
    name: 'SuggestionMovieItem',
    props: {
        suggest: Object,
        selected_movies:Array,
    },
    data() {
        return {
            imgURL: `https://image.tmdb.org/t/p/original/${this.suggest.poster_path}`
        }
    },
    computed: {
        isSelected() {
            return this.selected_movies?.includes(this.suggest)
        }
    }

}
</script>

<style scope>
img {
    cursor: pointer;
    width: 100%;
    height: 100%;
    padding: 10px;
}
#suggest-img {
    width: 200px;
    height: 300px;
}

#suggest-img figure {
    width: 100%;
    height: 100%;
    position: relative;
}

#suggest-img figcaption {
  padding: 10px;
  width: 100%; height: 100%;
  background-color: rgba(0,0,0,0.7);

  position: absolute; /* 이미지와 겹치게 처리 */
  top: 0; left: 0;

  color: #fff; 
  text-align: left ;

  opacity: 0; /* 처음엔 안보이고 */

  transition: 0.3s;
  display:flex;
  align-items: flex-end;

}

#suggest-img figcaption:hover , #collection-item figcaption:focus  {
  opacity: 1;
}


</style>