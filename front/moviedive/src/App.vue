<template>
  <div id="app">
    <NavVar/>
    <router-view/>
    <FooterInfo/>
  </div>
</template>


<script>
import NavVar from '@/components/NavVar.vue'
import FooterInfo from '@/components/FooterInfo.vue'

export default {
  name: 'App',
  components: {
    NavVar,
    FooterInfo
  }
}
</script>

<style>

@font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
    font-style: normal;
}

#app {
  font-family: 'Pretendard-Regular';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
