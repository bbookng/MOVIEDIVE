<template>
  <nav id="nav-bar" class="d-flex justify-content-between align-items-center text-light">
    <div style="width:26rem;" class="nav-left">
      <ul class="d-flex justify-content-between align-items-center mx-auto my-0 px-0" >
        <li class="logo">
          <router-link :to="{ name: 'main' }">
          <!-- <img src="https://moviedive.s3.ap-northeast-2.amazonaws.com/4dd.png" alt=""> -->
          <img src="https://moviedive.s3.ap-northeast-2.amazonaws.com/logo_bold.png" alt="">
          <!-- <img src="https://moviedive.s3.ap-northeast-2.amazonaws.com/logo_3d.png" alt=""> -->
          </router-link>         
        </li>
        <li>
          <router-link id="nav-item" :to="{ name: 'collection' }">컬렉션</router-link>
        </li>
        <li>
          <router-link id="nav-item" :to="{ name: 'community' }">커뮤니티</router-link>
        </li>
        <li>
          <router-link id="nav-item" :to="{ name: 'deepdive' }">DEEP DIVE</router-link>
        </li>
      </ul>
    </div>
    <div class="nav-right" style="width:30rem;">
      <ul class="d-flex justify-content-evenly align-items-center my-0">
        <li class="nav-item" v-if="isLoggedIn" style="position:relative" >
          <form @submit="searchThings(searchKeyword)">
            <div class="search-box">
              <div class="search-container">
                <input autocomplete="off" @input="changeKeyword" :value="searchKeyword" type="search" id="search" placeholder="🔍     영화 제목 또는 장르 입력" />
                  <auto-complete-suggestions id="suggestion-box" @titleFromSuggestions="fillSearchKeyword"></auto-complete-suggestions>
              </div>
            </div>
          </form>
        </li>
        <li class="nav-item" v-if="!isLoggedIn">
          <router-link :to="{ name: 'login' }">Login</router-link>
        </li>
        <li class="nav-item" v-if="!isLoggedIn">
          <router-link :to="{ name: 'signup' }">Signup</router-link>
        </li>
        <div v-if="isLoggedIn" class="nav-item btn-group">
          <img v-if="isLoggedIn" @click="myPage" class="profile-img" :src=imgURL alt="">
          <button v-if="isLoggedIn" type="button" class="dropdown-button btn btn-#fff dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"></button>
          <ul class="dropdown-menu" style="border-radius: 0px;">
            <li v-if="isLoggedIn">
              <button class="dropdown-item nav-item" @click="myPage">🏠 마이페이지</button>
            </li>
            <li v-if="isLoggedIn">
              <button class="dropdown-item nav-item" @click="profileModify">✏️ 프로필 관리</button>
            </li>
            <li v-if="isLoggedIn">
              <button class="dropdown-item nav-item" @click="accountModify">⚙️ 계정 설정</button>
            </li>
            <li v-if="isLoggedIn"><hr class="dropdown-divider"></li>
            <li v-if="isLoggedIn">
              <router-link class="dropdown-item nav-item" :to="{ name: 'logout' }" style="text-align:center; font-size:16px;">로그아웃</router-link>
            </li>
          </ul>
        </div>
      </ul>
    </div>
  </nav>
</template>


<script>
import { mapActions } from 'vuex'
import AutoCompleteSuggestions from '@/components/AutoCompleteSuggestions'

export default {
  name: 'NavVar',
  data() {
    return {
      searchKeyword: '',
    }
  },
  components: {
    AutoCompleteSuggestions
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    },
    currentUser() {
      return this.$store.getters.currentUser
    },
    username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    nickname() {
      return this.currentUser.profile_info ? this.currentUser.profile_info[0].nickname : 'guest'
    },
    mypage() {
      return this.$store.state.myPage
    },
    imgURL() {
      return this.currentUser.profile_img
    },
    
  },
  methods: {
    ...mapActions(['fetchMovies', 'autoComplete']),
    searchThings(keyword) {
      this.$router.push({ name: 'search_result', params: { keyword } })
    },
    fillSearchKeyword(suggest){
      this.searchKeyword = suggest.title
      this.movie = suggest.id
    },
    changeKeyword(event) {
      this.searchKeyword = event.target.value
      this.autoComplete(this.searchKeyword)
    },
    myPage() {
      this.$store.commit('GET_MY_PAGE', 1)
      this.$router.push({ name: 'mypage', params: { username: this.currentUser.username} })
    },
    profileModify() {
      this.$store.commit('GET_PROFILE_MODIFY', 2)
      this.$router.push({ name: 'mypage', params: { username: this.currentUser.username} })
    },
    accountModify() {
      this.$store.commit('GET_ACCOUNT_MODIFY', 3)
      this.$router.push({ name: 'mypage', params: { username: this.currentUser.username} })
    },
  }
}
</script>

<style scoped>
.logo {
  flex: none;
  width: 10rem;
  /* margin-top: 0.8rem; */
}

.profile-img {
  margin: auto;
  border-radius: 20px ;
  width: 3.5rem;
}

#nav-bar {
  height: 60px; 
  border-bottom: #e2e2e2 solid 3px;
  background-color: white;
}
  a {
    color: black;
    text-decoration: none;
    font-size:18px;
    font-weight: 400;
    margin: auto;
    flex: none;
  }
  ul {
    color: #fff;
    list-style:none;
  }

  .nav-item {
    flex: 1;
  }

  .nav-right {
    margin-top: 0;
  }

  .left-nav-item:hover {
    color: #6a6d72b7;
    /* font-weight: bolder; */
  }
  .right-nav-item:hover {
    color: #40444b;
    font-weight: bolder;
  }
  .router-link-exact-active{
    text-decoration: none;
  }

  .dropdown-item {
    color:black;
  }

  /* search box */
  .search-box{
    width: 300px;
    height: 40px;
    font-size:10px;
  }
  .search-container{
    margin-right: auto;
    width: 300px;
    vertical-align: middle;
    white-space: nowrap;
    position: relative;
    padding-right: 10px;
  }
  .search-container input#search{
    width: 57px;
    height: 40px;
    opacity: 75%;
    border: none;
    font-size: 12pt;
    float: right;
    padding-left: 20px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    color: #0c0c0c;
    transition: width .55s ease;
    border-radius: 0px;
  }
  .search-container input#search:-ms-input-placeholder {  
    color: white; 
    background-image: url(https://moviedive.s3.ap-northeast-2.amazonaws.com/search-icon.png);
  }  
  .search-container input#search:focus, .search-container input#search:active{
    outline:none;
    width: 100%;
  }  
  .search-container:hover input#search{
    width: 300px;
    background: #40444b;
    border: 1px solid black; 
  }  

  .search-container .icon {
    width: 2rem;
  }
  .search-container:hover .icon{
    color: #ff1717;
    background: #40444b;
    opacity: 1;
    width: 2rem;
  }
  .search-container .search-icon{
    padding-right:10px;
    background:black;
    position: absolute;
    border: none;
    top: -2px;
    left:82%;
    margin-left: 17px;
    margin-top: 6px;
    z-index: 1;
    color: rgb(214, 10, 10);
  }
  .search-container input#search:focus, .search-container input#search:active{
    outline:none;
    width: 300px;
  }
  .search-container:hover input#search{
    width: 300px;
    background: white;
  }
  .search-container:hover .search-icon{
    color: #e90a0a;
    opacity: 0.8;
    background: #40444b;
  }
  #suggestion-box {
    position:absolute;
    font-size:15px;
    width: 300px;
    opacity: 0;
    top:50px;
    left:20px;
    z-index: 5;
  }
  input#search:focus{
    width: 300px;
    background: #40444b;
  }
  .search-container:focus-within {
      opacity: 1;
  }
  .search-container:focus-within .search-icon{
    color: #ffffff;
    opacity: 0.8;
    background: #40444b;
  }

  /* Dark/Light mode toggle */
  .toggle-btn {
  position: relative;
  left: 1rem;
  width: 60px;
  height: 32px;
  margin: 0 auto;
  border-radius: 40px;
  }

  input[type="checkbox"] {
    width: 60%;
    height: 40%;
    position: absolute;
    top: 0px;
    left: 0px;
    right: 0px;
    bottom: 0px;
    cursor: pointer;
    opacity: 0;
    z-index: 2;
  }

  /* First toggle btn */

  #_1st-toggle-btn span {
    position: absolute;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    overflow: hidden;
    opacity: 1;
    background-color: #fff;
    box-shadow: 0px 2px 25px #d9d9d9;
    border-radius: 40px;
    transition: 0.2s ease background-color, 0.2s ease opacity;
  }

  #_1st-toggle-btn span:before,
  #_1st-toggle-btn span:after {
    content: "";
    position: absolute;
    top: 3.5px;
    width: 23.2px;
    height: 23.2px;
    border-radius: 50%;
    transition: 0.5s ease transform, 0.2s ease background-color;
  }

  #_1st-toggle-btn span:before {
    background-color: #fff;
    transform: translate(-46.2px, 0px);
    z-index: 1;
  }

  #_1st-toggle-btn span:after {
    background-color: #000;
    transform: translate(-23.2px, 0px);
    z-index: 0;
  }

  #_1st-toggle-btn input[type="checkbox"]:checked + span {
    background-color: #000;
  }

  #_1st-toggle-btn input[type="checkbox"]:active + span {
    opacity: 0.5;
  }

  #_1st-toggle-btn input[type="checkbox"]:checked + span:before {
    background-color: #000;
    transform: translate(-8.4px, -7.6px);
  }

  #_1st-toggle-btn input[type="checkbox"]:checked + span:after {
    background-color: #fff;
    transform: translate(0.6px, 0px);
  }

#nav-list {
  color: white;
}
</style>
