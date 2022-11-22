<template>
  <div>
    <GameHeader />
    <GameArea />
  </div>
</template>

<script>
import GameHeader from "@/components/game/GameHeader.vue";
import GameArea from "@/components/game/GameArea.vue";
export default {
  name: "PlayView",
  components: {
    GameHeader,
    GameArea,
  },
};
</script>

<style>
</style>