<template>
  <div id="startpage">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-card height="500px"></v-card>
          <v-flex xs4 class="grey lighten-4">
            <v-container style="position: relative;top: 13%;" class="text-xs-center">
              <v-card flat>
                <v-card-title primary-title>
                  <h3>Login</h3>
                </v-card-title>
                <v-card-text>
                  <v-form v-model="loginForm">
                    <v-text-field prepend-icon="person" :rules="formRules" v-model="email" label="Login" type="text"></v-text-field>
                    <v-text-field prepend-icon="lock" :rules="formRules" v-model="password" label="Password" id="password" type="password"></v-text-field>
                    <v-card-actions>
                      <div>
                        <router-link to="/">
                          <v-btn color="purple" style="margin-right: 20px" dark>Back</v-btn>
                        </router-link>
                      </div>
                      <div>
                       
                          <v-btn color="purple" v-on:click="submit()" dark>Login</v-btn>
                       
                      </div>
                    </v-card-actions>  
                  </v-form>
                </v-card-text>
              </v-card>
            </v-container>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <app-footer></app-footer>
  </div>
</template>

<script>
  import AppFooter from './AppFooter'
  //import{ signIn } from '@/helpers/login/login'
  export default {
    components: {
      AppFooter
    },
  data: () => ({
    loginForm: false,
    alert: false,
    email: "",
    password: "",
    e1: true,
    formRules: [
      v => !!v || "Mandatory Field"
      //v => (v && v.length <= 10) || "Name must be less than 10 characters"
    ]
  }),
  computed: {
    doneTodosCount() {
      return this.$store.getters.isLogged;
    }
  },
  methods: {
    submit: function() {
      //if (this.$refs.loginForm.validate()) {
        this.$store
          .dispatch("authLogin", {
            email: this.email.toLowerCase(),
            password: this.password,
            loggedin: true,
          })
          .catch(err => {
          this.alert = !this.$store.getters.authResult;
          throw err;
          });
      //}
    },
    clear: function() {
      this.email = null;
      this.password = null;
    }
  }
};
</script>