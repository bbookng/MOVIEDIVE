<template>
  <div v-if="collection" class="container" id="collection-detail-info">
    <div class="row ">
      <div class="col">
        <h3 id="collection-detail-title">{{ collection.title }}</h3>
        <p id="collection-detail-description">{{ collection.description }}</p>
      </div>
      <div class="col" v-if="currentUser.pk == collection.user.pk">
        <router-link :to="{ name: 'save_collection', params: { collectionPk: this.collection.pk } }">수정</router-link>
        <span><button @click="deleteCollection">삭제</button></span>
      </div>
    </div>
    <div id="collection-detail-statistics">
      <span>좋아요 {{ collection.like_users_cnt }}</span> | 
      <span> 댓글 수 {{ collection.comments_cnt }}</span> |
      <span> {{ collection.created_string }} 업데이트</span>
    </div>
    <div class="collection-detail-line"></div>
    <div id="button-container" class="d-flex justify-content-evenly align-items-center">
      <div class="collection-detail-button" @click="likeCollection">
        <img class="button like" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/heart.png" alt="">
        좋아요
      </div>
      <div class="collection-detail-button" @click="goCommentsList">
        <img class="button comment" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/comment.png" alt="">
        댓글
      </div>
      <div class="collection-detail-button">
        <img class="button comment" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/share.png" alt="">
        공유
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000/api'

export default {  
  name: "CollectionDetailInfo",
  data() {
    return {
      collection : null,
    }
  },
  created() {
    this.getCollection()
  },
  props:{
    currentUser: Object,
    collection_pk: String,
  },
  methods: {
    getCollection() {
      axios({
          method: 'get',
          url: `${API_URL}/collections/${this.collection_pk}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          } 
      })
      .then((res) => {
          this.collection = res.data
      })
      .catch((err) => {
          console.log(err)
      })
    },
    likeCollection() {
      // 컬렉션 좋아요 + 1
      axios({
        url: `${API_URL}/collections/${this.collection.pk}/like/`,
        method: 'post',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => { 
        this.getCollection(this.collection.pk)
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
        url: `${API_URL}/collections/${this.collection.pk}/`,
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
  cursor: pointer;
}
.collection-detail-button{
  font-size:20px;
  border: none;
  background-color: transparent;
  width: 30%;
}

.button {
  width: 20px;
  height: 20px;
}

</style>