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

import axios from 'axios';

axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  timeout: 1000,
  headers: {'X-Custom-Header': 'foobar'}
});

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



