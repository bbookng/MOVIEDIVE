<template>
  <div id="collection-detail">
    <h1> header img 들어갈 공간</h1>
    <hr>
    <h3> {{ collection.title }}</h3>
    <p>{{ collection.description }}</p>
    <p>
        <span>좋아요 수 </span>
        <span> 댓글 수 </span>
        <span> 몇 분 전 업데이트 ?</span>
    </p>
    <div>
        <button> 좋아요 </button>
        <button> 댓글 </button>
        <button> 공유 </button>
    </div>
    <div>
        <h3>작품들</h3>
    </div>
    <hr>
    <div>
        <p>댓글</p>
        <span>댓글 개수</span>
        <ul>
            <li> 댓글들 </li>
        </ul>
        <hr>
        <form action="submit">
            <input type="text" value="컬렉션에 댓글 남기기">
            <button> 등록 </button>
        </form>
    </div>


  </div>
</template>

<script>
export default {
    name: 'CollectionDetail',
    data() {
        return {
            collection_pk: this.$route.params.collection_pk,
        }
    },
    computed: {

    }
}
</script>

<style>

</style>