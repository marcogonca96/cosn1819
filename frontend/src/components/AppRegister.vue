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
                                    <h3>Registration</h3>
                                </v-card-title>
                                <v-card-text>
                                    <v-form v-model="formCreateUser" ref="formCreateUser" lazy-validation>
                                        <v-text-field v-model="name" :error-messages="nameErrors"  label="Name" required @input="$v.name.$touch()" @blur="$v.name.$touch()"></v-text-field>
                                        <v-text-field v-model="email" :error-messages="emailErrors" label="E-mail" required @input="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
                                        <v-text-field v-model="password" :error-messages="emailErrors" label="Password" required @input="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
                                        <v-text-field v-model="confirmpassword" :error-messages="emailErrors" label="Confirm Password" required @input="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
                                        <v-checkbox v-model="checkbox" :error-messages="checkboxErrors" label="Upgrade for Premium?" required @change="$v.checkbox.$touch()" @blur="$v.checkbox.$touch()"></v-checkbox>
                                        <v-card-actions>
                                            <div>
                                            <router-link to="/">
                                                <v-btn color="purple" style="margin-right: 20px" dark>Back</v-btn>
                                            </router-link>
                                            </div>
                                            <div>
                                             
                                                <v-btn color="purple" v-on:click="submit()" dark>Registration</v-btn>
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
    import axios from 'axios'

    import { createUser } from "@/helpers/register/register.js";

    
    export default {
        components: {
            AppFooter
        },
    
    
  
    data: () => ({
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters'
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4'
      ],
      formCreateUser: [],
      confirmpassword: '',
      password: '',
      password_rules: [
          v => !!v || 'Password is required',
      ],
      checkbox: false
    }),

    methods: {
      submit () {
        if (this.$refs.formCreateUser.validate()) {
          // Native form submission is not yet supported
          createUser(this.name, this.password, this.email, 'Admin').then(suc => {
              console.log("registou");
          }).catch(err => {
              throw err;
          })
        }
      },
      clear () {
        this.$refs.form.reset()
      }
    }
  }
</script>
