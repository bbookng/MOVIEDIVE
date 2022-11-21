<template>
    <div id="collection-detail" class="container">
      <div id="collection-bg-img-box" class="row">
        <img id="collection-bg-img" :src=mainPosterURL alt="" class="col">
      </div>
      <hr>
      <h3>{{ collection.title }}</h3>
      <p>{{ collection.description }}</p>
      <p>
        <span>좋아요 {{ collection.like_users_cnt }}</span> | 
        <span> 댓글 수 {{ collection.comments_cnt }}</span> |
        <span> {{ collection.created_string }} 업데이트</span>
      </p>
      <div v-if="currentUser.pk == collection.user.pk">
        <router-link :to="{ name: 'save_collection' }">수정</router-link>
        <button @click="deleteCollection">삭제</button>
      </div>
      <div>
        <button @click="likeCollection">좋아요</button>
        <button @click="goCommentsList">댓글</button>
        <button>공유</button>
      </div>
      <hr>
      <div>
        <h3>작품들</h3>
        <div v-for=" suggest in collection.movies " :key="suggest.pk" >
          <SuggestionMovieItem :suggest="suggest"/>
          {{ suggest.title }}
        </div>
      </div>
      <hr />
      <div id="commentSet">
        <p>댓글 <span>{{ collection.comments_cnt }}</span> </p>
        {{ collection.comments}}
        <ul>
          <div v-for="comment in collection.collection_comments" :key="comment.pk">
            <li>{{ comment.content }} <span>{{ comment.created_string }}</span> </li>
          </div>
        </ul>
        <hr />
        <form @submit.prevent="createComment">
          <input v-model="comment_content" type="text" placeholder="컬렉션에 댓글 남기기" />
          <input type="submit">
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import SuggestionMovieItem from '@/components/collections/SuggestionMovieItem'
  
  const API_URL = 'http://127.0.0.1:8000/api'

  export default {
    name: "CollectionDetailView",
    components: {
      SuggestionMovieItem
    },
    data() {
      return {
        collection: null,
        mainPosterURL: null,
        suggest: null,
        comment_content: null,
      };
    },
    computed: {
      currentUser() {
        return this.$store.getters.currentUser
      },
      collection_pk() {
        return this.$route.params.collectionPk
      }
    },
    methods: {
      getCollection(collection_pk) {
        
        axios({
          url: `${API_URL}/collections/${collection_pk}/`,
          method: 'get',
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res)=>{
          this.collection = res.data
          this.mainPosterURL = `https://image.tmdb.org/t/p/original/${res.data.movies[0].backdrop_path}`
        })
      },
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
      createComment() {
        const content = this.comment_content
  
        if (!content) {
          alert('내용을 입력해주세요')
          return
        } 
  
        axios({
          url: `${API_URL}/collections/${this.collection_pk}/comments/create/`,
          method: 'post',
          data: { content },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
          this.getCollection(this.collection_pk)
          this.comment_content = null
          console.log(res.data)
        })
  
      },
      goCommentsList() {
        // 댓글 div 로 이동
        const commentbox = document.getElementById("commentSet")
        commentbox.scrollIntoView({behavior: 'smooth'})
      },
      // updateCollection() {
        
      // },
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
      
    },
    created() {
      this.getCollection(this.collection_pk)
    },
    // destroyed() {
    //   this.$store.commit("SET_ISCOLLECTION_DETAIL", false);
    // },
  };
  </script>
  
  <style>
  #collection-detail {
    width: 80vw;
    border: black 1px;
  }
  
  #collection-bg-img-box {
    width:80%;
    height:500px;
    overflow: hidden;
    margin:0 auto;
  }
  
  #collection-bg-img {
    width:100%;
    height:100%;
    object-fit: cover;
  }
  </style>