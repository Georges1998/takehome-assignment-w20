<template>
  <div>
    <Instructions v-bind:complete="true"/>
    <Show
      v-for="show in shows"
      :key="show.id"
      :id="show.id"
      :name="show.name"
      :episodes_seen="show.episodes_seen"
    />
    <Counter v-bind:episodes_seen="counts" :message="message" />
    <input v-model="showName" placeholder="Show Name">
    <input type="number" v-model="episodes" placeholder="Episodes Seen">
    <button  v-on:click="createShow(showName,episodes)">Add Show</button>
  </div>
</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";
import Counter from "./Counter.vue";

export default {
  components: {
    Instructions,
    Counter,
    Show
  },
  data() {
    return {
      shows: [
        { id: 1, name: "Game of Thrones", episodes_seen: 0 },
        { id: 2, name: "Naruto", episodes_seen: 220 },
        { id: 3, name: "Black Mirror", episodes_seen: 3 }
      ],
      message: "I'm a Counter!",
      counts: 0
    };
  },
  methods: {
        createShow: function(showName, episodes=0) {
          var newId = this.shows[this.shows.length-1].id + 1;
          this.shows.push({id: newId, name: showName,episodes_seen: episodes });
          }

          }
};
</script>

<style>
</style>


