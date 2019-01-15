<template>
  <v-card
    class="mx-auto elevation-20"
    style="max-width: 400px;padding:0px"      
  >
    <v-layout justify-space-between>
      <v-flex xs8>
        <v-card-title primary-title>
          <div>
            <div class="headline"> {{ trailer.title }}</div>
            <div>{{ categories.join(', ') }}</div>
          </div>
        </v-card-title>
      </v-flex>
      <v-img
        class="shrink ma-2"
        contain
        height="125px"
        v-bind:src=(trailer.image)
        style="flex-basis: 125px"
      ></v-img>
    </v-layout>
    <v-divider dark></v-divider>
    <v-card-actions class="pa-3">
      Rate this album
      <v-spacer></v-spacer>
    <div class="ml-2 grey--text text--darken-2">
        ({{ trailer.rating }})
      </div>
      <v-rating
        v-model="trailer.rating"
        color="yellow accent-4"
        dense
        half-increments
        hover
        readonly
        size="18"
      ></v-rating>
      <v-spacer></v-spacer>
      <router-link :to="{ name: 'trailer', params: { trailerID: trailer.id }}">
          <v-btn  icon class="mr-0">
           <v-icon dark >mdi-chevron-right</v-icon>
          </v-btn>
       </router-link>
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {
    props: ['trailer', 'categories']     
  }
</script>
