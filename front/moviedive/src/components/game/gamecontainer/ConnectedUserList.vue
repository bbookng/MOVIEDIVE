<template>
  <div id="connected-users-list">{{ connectedUsers }}</div>
</template>

<script>
export default {
  name: "ConnectedUserList",
  props: {
    connectedUsers: Array,
  },
};
</script>

<style>
#connected-users-list {
  border: solid 1px black;
  height: 100%;
}
</style>