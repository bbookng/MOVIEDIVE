<template>
  <div id="app">
      <NavVar/>
      <router-view style="height:2160px;"/>
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

</style>
