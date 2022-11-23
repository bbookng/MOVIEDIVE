<template>
  <div id="app">
    <!-- <div>
      <DiveView id="diveview" v-if="!diving" @logo-clicked="goToMain"/>
    </div> -->
    <!-- <div v-if="diving"> -->
      <NavVar/>
      <router-view/>
      <FooterInfo/>
    <!-- </div> -->
  </div>
</template>


<script>
import NavVar from '@/components/NavVar'
import FooterInfo from '@/components/FooterInfo'
// import DiveView from '@/views/DiveView'

export default {
  name: 'App',
  components: {
    NavVar,
    FooterInfo,
    // DiveView,
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
    font-weight: 100 800;
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

.container {
  display: flex;
}

</style>
