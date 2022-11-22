<template>
  <div id="game-area">
    <GameContainer />
  </div>
</template>

<script>
import GameContainer from "@/components/game/GameContainer.vue";

export default {
  name: "GameArea",
  components: {
    GameContainer,
  },
};
</script>

<style>
#game-area {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5vh;
}
</style>