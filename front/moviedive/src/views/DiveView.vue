<template>
  <div>
    <DiveCanvas @logo-clicked="logoClicked"/>
  </div>
</template>

<script>
import DiveCanvas from '@/components/DiveCanvas'

export default {
  name: 'DiveView',
  components: {
    DiveCanvas,
  },
  methods: {
    logoClicked() {
      this.$router.push({ name: 'main' })
      this.$emit('logo-clicked')
    }
  }
}
</script>

<style>

</style>