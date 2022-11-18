<template>
  <nav class="d-flex justify-content-between align-items-center text-light my-4">
    <div style="width:27rem;" class="nav-left">
      <ul class="d-flex justify-content-between align-items-center my-0 px-0" >
        <li class="m-0">
          <router-link :to="{ name: 'main' }">LOGO</router-link>         
        </li>
        <li>
          <router-link :to="{ name: 'collection' }">Collection</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'community' }">Community</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'play' }">Play</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'deepdive' }">DEEP DIVE</router-link>
        </li>
      </ul>
    </div>
    <div class="nav-right" style="width:18rem;">
      <ul class="d-flex justify-content-end align-items-center my-0">
        <li v-if="!isLoggedIn" class="mx-3">
          <router-link :to="{ name: 'login' }" class="right-nav-item">Login</router-link>
        </li>
        <li v-if="!isLoggedIn" class="mx-1">
          <router-link :to="{ name: 'signup' }" class="right-nav-item">Signup</router-link>
        </li>

        

        <li v-if="isLoggedIn" style="position:relative" >
          <form @submit="searchThings(searchKeyword)">
            <div class="search-box">
              <div class="search-container">
                  <button class="search-icon"><i class="bi bi-search"></i></button>
                  <input autocomplete="off" @input="changeKeyword" :value="searchKeyword" type="search" id="search" placeholder="Search..." />
                  <auto-complete-suggestions id="suggestion-box" @titleFromSuggestions="fillSearchKeyword"></auto-complete-suggestions>
              </div>
            </div>
          </form>
        </li>
        
        <div v-if="isLoggedIn" class="btn-group">
          <button type="button" class="btn btn-danger"></button>
          <button type="button" class="btn btn-danger dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
            <span class="visually-hidden">프로필이미지</span>
          </button>
          <ul class="dropdown-menu">
            <li><router-link class="dropdown-item" :to="{ name: 'mypage' }">MyPage</router-link></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </div>

        <!-- 크기 수정 필요해요.. 할 줄 모르겠어 ㅠ ㅠ -->
        <li v-if="isLoggedIn">
          <div class="toggle-btn" id="_1st-toggle-btn" style="position:relative">
            <input type="checkbox">
            <span></span>
          </div>
        </li>

      </ul>
    </div>
  </nav>
  
</template>

<script>
import AutoCompleteSuggestions from '@/components/AutoCompleteSuggestions'

export default {
  name: 'NavVar',
  data() {
    return {
      searchKeyword: "",
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
  },
  methods: {
    fillSearchKeyword(keyword){
      this.searchKeyword = keyword
    },
    changeKeyword(event) {
      this.searchKeyword = event.target.value
      this.autoComplete(this.searchKeyword)
    },
  },
}
</script>

<style scoped>
  a {
    color: rgb(19, 18, 18);
    text-decoration: none;
    font-size:20px;
    font-weight: 400;
  }
  ul {
    list-style:none;
  }
  .left-nav-item:hover {
    color: #40444b;
    font-weight: bolder;
  }
  .right-nav-item:hover {
    color: #40444b;
    font-weight: bolder;
  }
  .router-link-exact-active{
    font-weight: bold;
    text-decoration: none;
  }
  .dropdown-item {
    color:black;
  }

  /* search box */
  .search-box{
    width: 300px;
    height: 40px;
    font-size:20px;
  }
  .search-container{
  width: 300px;
  vertical-align: middle;
  white-space: nowrap;
  position: relative;
  }
  .search-container input#search{
    width: 50px;
    height: 40px;
    background: black;
    border: none;
    font-size: 15pt;
    float: right;
    color: #ff0000;
    padding-left: 20px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    color: #0c0c0c;
    transition: width .55s ease;
  }
  .search-container input#search:-ms-input-placeholder {  
    color: #40444b;  
  }  
  .search-container input#search:focus, .search-container input#search:active{
    outline:none;
    width: 300px;
  }  
  .search-container:hover input#search{
    width: 300px;
    background: #40444b;
  }  
  .search-container:hover .icon{
    color: #ff1717;
    background: #40444b;
    opacity: 1;
  }
  #suggestion-box {
    position:absolute;
    /* visibility: hidden; */
    left:20px;
    z-index: 5;
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
    background: #40444b;
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
  .search-container:focus-within #suggestion-box {
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
  width: 58px;
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
    margin: 0px;
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
    transform: translate(-23.2px, 0px);
    z-index: 1;
  }

  #_1st-toggle-btn span:after {
    background-color: #000;
    transform: translate(3.2px, 0px);
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
    transform: translate(22.4px, -7.6px);
  }

  #_1st-toggle-btn input[type="checkbox"]:checked + span:after {
    background-color: #fff;
    transform: translate(31.6px, 0px);
  }

  
</style>
