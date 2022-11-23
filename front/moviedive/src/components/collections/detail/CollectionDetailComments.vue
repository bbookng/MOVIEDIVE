<template>
  <div v-if="collection" id="collection-detail-comments">
    <div id="commentSet">
      <div>
        <p>댓글 <span>{{ collection.comments_cnt }}</span> </p>
      </div >
      <div class="d-flex flex-column">
        <ul>
          <div v-for="comment in collection.collection_comments" :key="comment.pk">
              <div>
                <router-link class="comment-user" :to="{ name: 'mypage', params: { username: comment.user.username} }">
                  <img class="comment-user-profileimg" :src=comment.user.profile_img alt="...">
                </router-link>
              </div>
              <div>
                <div>
                  <router-link class="comment-user" :to="{ name: 'mypage', params: { username: comment.user.username} }">{{ comment.user.nickname }}</router-link> <span>{{ comment.created_string }}</span>
                </div>
              </div>
              <div>
                {{ comment.content }}
              </div>
          </div>
        </ul>
      </div>
          
        <hr />
        <form @submit.prevent="createComment">
          <input id="comment-input" v-model="comment_content" type="text" placeholder="컬렉션에 댓글 남기기" />
          <input id="comment-button" class="btn btn-outline-dark rounded-circle" type="submit" value="등록">
        </form>
      </div>
    
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000/api'
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
#collection-detail-comments{
    border: solid black 1px;
}

.comment-user-profileimg {
  width: 10%;
  height: 10%;

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