<template>
<div>
  <p>{{message}} {{episodes_seen}}<button  v-on:click="increment"> increment</button>  <button  v-on:click="decrement"> decrement</button></p>
</div>
</template>

<script>
export default {
  props:{episodes_seen: Number, message: String},
  data() {
    return {
      count: 0
    };
  },
  methods: {
    increment: function () {
      this.episodes_seen++
    },
    decrement: function () {
      this.episodes_seen--
    }
  }
};
</script>

<style>
</style>

