<template>
  <div id="collection-detail">
    <h1>header img 들어갈 공간</h1>
    {{collection}}
    <hr />
    <h3>{{ collection.title }}</h3>
    <p>{{ collection.description }}</p>
    <p>
      <span>좋아요 {{ collection.like_users_cnt }}</span> | 
      <span> 댓글 수 {{ collection.comments_cnt }}</span> |
      <span> {{ collection.created_string }}전 업데이트</span>
    </p>
    <div>
      <!-- <button @click="likeCollection">좋아요</button>
      <button @click="goCommentsList">댓글</button> -->
      <button>공유</button>
    </div>
    <div>
      <h3>작품들</h3>
    </div>
    <hr />
    <div>
      <p>댓글</p>
      <span>댓글 개수</span>
      <ul>
        <li>댓글들</li>
      </ul>
      <hr />
      <form action="submit">
        <input type="text" value="컬렉션에 댓글 남기기" />
        <button>등록</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "CollectionDetail",
  data() {
    return {
      collection: null,
    };
  },
  computed: {},
  props: {
    collection_pk: Number,
  },
  methods: {
    getCollection(collection_pk) {
      const API_URL = 'http://127.0.0.1:8000/api'

      axios({
        url: `${API_URL}/collections/${collection_pk}/`,
        method: 'get',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        this.collection = res.data
      })
    },
    // likeCollection() {
    //   // 컬렉션 좋아요 + 1

    // },
    // goCommentsList() {
    //   // 댓글 div 로 이동
    // }
    
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
</style>