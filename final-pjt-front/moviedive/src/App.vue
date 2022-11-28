<template>
  <div id="app" class="gradient">
      <NavVar/>
      <router-view />  
      <FooterInfo/>
  </div>
</template>


<script>
import NavVar from '@/components/NavVar'
import FooterInfo from '@/components/FooterInfo'

export default {
  name: 'App',
  components: {
    NavVar,
    FooterInfo,
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

<style scoped>
@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.6/dist/web/variable/pretendardvariable.css");

#app {
  font-family: 'Pretendard Variable';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
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

.gradient {
/* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
background: linear-gradient(to bottom, #ABC0E4, #F6F8FC)
}

</style>
