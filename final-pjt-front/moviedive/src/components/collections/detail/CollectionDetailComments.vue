<template>
  <div v-if="collection" id="collection-detail-comments">
    <div id="commentSet">
      <div class="comment-cnt" style="margin:0; padding-left:20px;padding-right:20px;">
        <h5 style="border-bottom:solid 1px black; padding-left:10px; padding-bottom:20px;">댓글 <span style="font-size: 15px;">{{ collection.comments_cnt }}</span> </h5>
      </div >
      <div class="comment-list-top">
        <div v-for="comment in collection.collection_comments" :key="comment.pk">
          <div class="d-flex collection-comment">
            <router-link class="comment-user" :to="{ name: 'mypage', params: { username: comment.user.username} }">
              <img class="comment-user-profileimg" :src=comment.user.profile_img alt="...">
            </router-link>
            <div style="width:100%">
              <div class="comment-top d-flex justify-content-between">
                <router-link class="comment-user" :to="{ name: 'mypage', params: { username: comment.user.username} }">{{ comment.user.nickname }}</router-link> 
                <p class="my-0">{{ comment.created_string }}</p>
              </div>
              <div class="collection-comment-content d-flex justify-content-start">
                <p class="my-0">{{ comment.content }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
          
        <hr />
        <form @submit.prevent="createComment">
          <input id="comment-input" v-model="comment_content" type="text" placeholder="컬렉션에 댓글 남기기" />
          <input id="comment-button" class="btn btn-outline-dark-sm" type="submit" value="등록">
        </form>
      </div>
    
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'https://moviedive.co.kr/api'
export default {
  name: "CollectionDetailComments",
  data() {
    return {
      comment_content: null,
      collection: null,
      comment_user: null,
    }
  },
  computed: {
    
  },
  props: {
    collection_pk: String,
  },
  created() {
    this.getCollection(this.collection_pk)
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
    createComment() {
      const content = this.comment_content

      if (!content) {
        alert('내용을 입력해주세요')
        return
      } 

      axios({
        url: `${API_URL}/collections/${this.collection.pk}/comments/create/`,
        method: 'post',
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.getCollection(this.collection.pk)
        this.comment_content = null
        console.log(res.data)
      })
    },
  }
}
</script>

<style scoped>

.collection-comment {
  width: 100%;
  margin-top:10px;
  border-bottom:1px black solid;
}
.comment-cnt {
  text-align: left;
  padding-top: 1rem;
  padding-left: 1rem;
  margin-left: 20px;
  margin-bottom: 0;
}

.comment-top{
  width: 100%;
}
#collection-detail-comments{
    margin-left:15%;
    margin-right:15%
}
.comment-list-top{
  margin-left:20px;
  margin-right: 20px;
}
.comment-user-profileimg {
  width: 10%;
  height: 10%;
  border-radius: 50%;
  height: 60px;
  width: 60px;
  margin:0;
}

.comment-user {
  text-decoration: none;
  color: black;
}

#comment-input {
  width: 500px;
  height: 35px;
  border-radius: 10px;
  border: none;
  background-color: rgba(220, 220, 220, 0.322);
  margin-right: 10px;
  margin-bottom: 10px;
  padding: 1rem;
}

</style>