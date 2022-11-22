<template>
  <div id="collection-detail-comments">
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
const API_URL = 'http://127.0.0.1:8000/api'
export default {
  name: "CollectionDetailComments",
  props: {
    collection: Object,
  },
  data() {
    return {
      comment_content: null,
    }
  },
  methods: {
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
  }
}
</script>

<style>
#collection-detail-comments{
    border: solid black 1px;
}
</style>