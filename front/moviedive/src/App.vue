<template>
  <div id="app">
    <div>
      <DiveView id="diveview" v-if="!diving" @logo-clicked="goToMain"/>
    </div>
    <div v-if="diving">
      <NavVar/>
      <router-view/>
      <FooterInfo/>
    </div>
  </div>
</template>


<script>
import NavVar from '@/components/NavVar'
import FooterInfo from '@/components/FooterInfo'
import DiveView from '@/views/DiveView'

export default {
  name: 'App',
  components: {
    NavVar,
    FooterInfo,
    DiveView,
  },
  data() {
    return {
      diving: false,
    }
  },
  methods: {
    goToMain() {
      this.diving = true
    }
  },
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
