<template>
  <div id="MainTrailer">
    <div>
        메인 트레일러 들어갈 곳
    </div>
    <NewMovieList/>
  </div>
</template>

<script>
import NewMovieList from '@/components/main/NewMovieList.vue'

export default {
    name: 'MainTrailer',
    components:{
        NewMovieList,
    }

}
</script>

<style>
#MainTrailer {
    width: 100%;
    height: 970px;
    border: solid 1px black;
    background-color: blanchedalmond;
}
</style>