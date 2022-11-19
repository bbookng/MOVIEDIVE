<template>
  <div id="collection-detail" class="row">
    <div id="collection-bg-img-box">
      <img id="collection-bg-img" :src=mainPosterURL alt="">
    </div>
    <hr>
    <h3>{{ collection.title }}</h3>
    <p>{{ collection.description }}</p>
    <p>
      <span>좋아요 {{ like_cnt }}</span> | 
      <span> 댓글 수 {{ collection.comments_cnt }}</span> |
      <span> {{ collection.created_string }} 업데이트</span>
    </p>
    <div>
      <button @click="likeCollection(collection.pk)">좋아요</button>
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

export default {
  name: "CollectionDetail",
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
    like_cnt () {
      return this.collection.like_users_cnt
    }
  },
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
        this.mainPosterURL = `https://image.tmdb.org/t/p/original/${res.data.movies[0].backdrop_path}`
      })
    },
    likeCollection() {
      const API_URL = 'http://127.0.0.1:8000/api'
      // 컬렉션 좋아요 + 1
      axios({
        url: `${API_URL}/collections/${this.collection_pk}/like/`,
        method: 'post',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res.data)
        this.like_cnt = res.data.like_users_cnt
       
      })

    },
    createComment() {
      const API_URL = 'http://127.0.0.1:8000/api'
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
        console.log(res.data)
      })

    },
    goCommentsList() {
      // 댓글 div 로 이동
      const commentbox = document.getElementById("commentSet")
      commentbox.scrollIntoView({behavior: 'smooth'})
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