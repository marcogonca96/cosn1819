<template>
<v-app dark>

  <div id="app">
    <div></div>
    <main>
    <router-view/>
    </main>
  </div>
  </v-app>
</template>


<script>

export default {
  name: 'app'
}
</script>
<style>

#startpage{
  background-image: url('./assets/moviestiles.jpg');
    background-repeat: repeat;
    padding-bottom: 100%;
 opacity: 0.8;
}

</style>



