<template>
  <div>
    <footer>
      <p>
        ⓒ All copyrights reserved by
        <span><a href="mailto:gabodjango@gmail.com">GABODJANGO</a></span>
      </p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'FooterInfo',
}
</script>

<style scoped>
footer {
  display: flex;
  justify-content: center;
  margin: 5rem 0 2rem 0;
  color: #050505;
}
a {
  text-decoration: none;
  color: #111010;
}
a:hover {
  color: #181aa5;
}
</style>