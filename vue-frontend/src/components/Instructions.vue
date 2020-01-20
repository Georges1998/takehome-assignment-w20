<template>
  <div>
    <p>
      Pass a 'complete' prop to the instructions component in
      <code>src/App.vue</code>. See the README for more details. If you are successful, you'll see another line below saying you've completed this part.
    </p>
    <br />
    <p v-if="complete">Completed Part 1!</p>
  </div>
</template>

<script>
export default {
  props: {complete: Boolean}
};
</script>

<style>
</style>
