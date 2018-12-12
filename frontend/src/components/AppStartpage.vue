<template>
  <div id="startpage">
    <v-container>
     <v-toolbar dark>
        <v-toolbar-title class="white--text" style="color: #3c0068; font-size:60px">Trailerflix</v-toolbar-title>
        <v-spacer></v-spacer>
  
   <v-toolbar-items style="vertical-align: middle;margin-top:3%">
        <div class="text-xs-center" style="margin-top:3%">
          <v-layout row child-flex wrap>
              <div style="vertical-align: middle">
                <router-link to="/register">
                  <v-bottom-sheet>
                    <v-btn style="margin-right: 20px" slot="activator" color="purple" dark>
                      Register
                    </v-btn>
                  </v-bottom-sheet>
                </router-link>
                <router-link to="/login">
                  <v-bottom-sheet>
                    <v-btn slot="activator" color="purple" dark>
                      Login
                    </v-btn>
                  </v-bottom-sheet>
                </router-link>
              </div>
      </v-layout>
      </div>
       </v-toolbar-items>
       </v-toolbar>
      <app-footer></app-footer>
  
    </v-container>
  </div>
</template>

<script>
  import AppFooter from './AppFooter'
  
  export default {
    components: {
      AppFooter
    },
  
  }
</script>

<style>
  
</style>
