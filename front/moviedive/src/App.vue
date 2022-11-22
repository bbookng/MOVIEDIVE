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
  /* background-color: #000911; */
}

nav {
  padding: 30px;
}

nav a.router-link-exact-active {
  color: #767880;
}
</style>
