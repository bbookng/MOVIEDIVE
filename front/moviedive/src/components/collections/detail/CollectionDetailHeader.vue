<template>
  <div id="collection-detail-header" class="row">
      <img id="collection-bg-img" :src=url alt="">
  </div>
</template>
  
<script>
export default {
    name: "CollectionDetailHeader",
    props:{
      url: String,
    }
  }
</script>

<style>
#collection-detail-header{
  overflow: hidden;
  max-height: 35vh;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}
#collection-bg-img{
  max-height: initial;
  margin-top: -5vh;
}
</style>