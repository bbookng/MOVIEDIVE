<template>
  <div>
    <div>
      {{ currentuser }}
    </div>
  </div>
  
</template>

<script>
export default {
  name: 'MyPageView',
  computed: {
    currentuser() {
      return this.$store.getters.currentuser
    }

  },
  methods: {

  },
  created() {

  }

}
</script>

<style>

</style>