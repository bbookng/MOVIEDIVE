<template>
  <div id="collection-detail-info">
    <h3 id="collection-detail-title">{{ collection.title }}</h3>
    <p id="collection-detail-description">{{ collection.description }}</p>
    <div id="collection-detail-statistics">
      <span>좋아요 {{ collection.like_users_cnt }}</span> | 
      <span> 댓글 수 {{ collection.comments_cnt }}</span> |
      <span> {{ collection.created_string }} 업데이트</span>
    </div>
    <div v-if="currentUser.pk == collection.user.pk">
      <router-link :to="{ name: 'save_collection' }">수정</router-link>
      <button @click="deleteCollection">삭제</button>
    </div>
    <div class="collection-detail-line"></div>
    <div id="button-container" class="d-flex justify-content-evenly align-items-center">
      <button class="collection-detail-button" @click="likeCollection">좋아요</button>
      <button class="collection-detail-button" @click="goCommentsList">댓글</button>
      <button class="collection-detail-button">공유</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000/api'

export default {  
name: "CollectionDetailInfo",
props:{
  collection: Object,
  currentUser: Object,
},
methods: {
  likeCollection() {
    // 컬렉션 좋아요 + 1
    axios({
      url: `${API_URL}/collections/${this.collection_pk}/like/`,
      method: 'post',
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
    })
    .then((res) => { 
      this.getCollection(this.collection_pk)
      console.log(res.data)
    })
  },
  goCommentsList() {
    // 댓글 div 로 이동
    const commentbox = document.getElementById("commentSet")
    commentbox.scrollIntoView({behavior: 'smooth'})
  },
  deleteCollection() {
    if (confirm('정말 삭제하시겠습니까?') == true) {
      axios({
      method: 'delete',
      url: `${API_URL}/collections/${this.collection_pk}/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
    })
      .then(() => {
        this.$router.push({ name: 'collection' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
}
</script>

<style>
#collection-detail-info{
  display:flex;
  flex-direction: column;
  align-items: flex-start;
  border: solid black 1px;
  margin-left: 15%;
  margin-right: 15%;
}
#collection-detail-title{
  padding-left:10px;
  padding-right:10px;
  font-size: 30px;
  font-weight: 300;
}
#collection-detail-description{
  padding-left:10px;
  padding-right:10px;
}
#collection-detail-statistics{
  padding-left:10px;
  padding-right:10px;
}
.collection-detail-line{
  border: 0.5px black solid;
  width:100%;
}
#button-container{
  padding-top:10px;
  padding-bottom:10px;
  width:100%;
}
.collection-detail-button{
  font-size:20px;
  border: none;
  background-color: transparent;
  width: 30%;
}
</style>