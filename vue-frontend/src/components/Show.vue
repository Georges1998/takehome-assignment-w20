<template>
  
  <div><div>id: {{id}}</div> Name: {{name}}<Counter v-bind:episodes_seen="episodes_seen" :message="message"/></div>
</template>

<script>
import Counter from "./Counter.vue";
export default {
  data() {
    return {
      message: "Episodes Seen:",
    };
  },
  components: {
    
   Counter },
  name: "Show",
  props: {id: Number, name: String,episodes_seen: Number}
};
</script>

<style>
</style>
