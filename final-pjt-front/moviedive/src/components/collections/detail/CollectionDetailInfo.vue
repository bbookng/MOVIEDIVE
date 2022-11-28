<template>
  <div v-if="collection"  id="collection-detail-info">
    <div id="collection-detail-info-top" class="d-flex justify-content-between align-items-start" >
      <div style="padding: 5px;">
        <h3 id="collection-detail-title">{{ collection.title }}</h3>
        <p id="collection-detail-description" style="text-align:left; margin-left:5px;">{{ collection.description }}</p>
      </div>
      <div v-if="currentUser.pk == collection.user.pk">
        <router-link style="text-decoration: none; color:black;" :to="{ name: 'save_collection', params: { collectionPk: this.collection.pk } }">수정</router-link>
        <span><button class="delete-button" @click="deleteCollection">삭제</button></span>
      </div>
    </div>
    <div id="collection-detail-statistics">
      <span class="mx-2">좋아요 {{ collection.like_users_cnt }}</span> | 
      <span class="mx-2"> 댓글 {{ collection.comments_cnt }}</span> |
      <span > {{ collection.created_string }} 업데이트</span>
    </div>
    <div class="collection-detail-line"></div>
    <div id="button-container" class="d-flex justify-content-evenly align-items-center">
    <div class="collection-detail-button" @click="likeCollection">
        <img v-if="!userLike" class="button like" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/icon/heart+(3).png" alt="">
        <img v-if="userLike" class="button like" src="https://moviedive.s3.ap-northeast-2.amazonaws.com/icon/heart+(2).png" alt="">
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
const API_URL = 'https://moviedive.co.kr/api'

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
  computed: {
    userLike() {
      return this.collection.like_users.find((lu) => {
        return lu.pk == this.currentUser.pk
      }) ? true : false
    }

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
  margin-left: 15%;
  margin-right: 15%;
}
#collection-detail-info-top{
  width:100%;
  padding-left:10px;
  padding-right:10px;
  padding-top:10px;
}

#collection-detail-title{
  font-size: 30px;
  font-weight: bold 500;
}

#collection-detail-statistics{
  padding-left:10px;
  padding-right:10px;
  margin-bottom: 15px;
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

.collection-detail-button .button {
  width: 40px;
  height: 40px;
} 

.delete-button {
  border: none;
  background-color: transparent;
}

</style>