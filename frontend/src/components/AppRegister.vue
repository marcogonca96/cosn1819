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
                                        <v-text-field v-model="name" :rules="nameRules"  label="Name" required @input="$v.name.$touch()" @blur="$v.name.$touch()"></v-text-field>
                                        <v-text-field v-model="email" :rules="emailRules" label="E-mail" required @input="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
                                        <v-text-field :type="'password'" v-model="password" :rules="passwordRules" label="Password" required @input="$v.password.$touch()" @blur="$v.password.$touch()"></v-text-field>
                                        <v-text-field v-model="confirmpassword" :rules="confirmpassRules" label="Confirm Password" required @input="$v.confirmpassword.$touch()" @blur="$v.confirmpassword.$touch()"></v-text-field>
                                        <v-checkbox v-model="checkbox" label="Upgrade for Premium?" required @change="$v.checkbox.$touch()" @blur="$v.checkbox.$touch()"></v-checkbox>
                                        <v-card-actions>
                                            <div>
                                            <router-link to="/">
                                                <v-btn color="purple" style="margin-right: 20px" dark>Back</v-btn>
                                            </router-link>
                                            </div>
                                            <div>
                                                <v-btn color="purple" :disabled="!valid" v-on:click="submit()" dark>Registration</v-btn>
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
    import { createUser } from "@/helpers/register/register.js";

    
    export default {
        components: {
            AppFooter
        },
    
    
  
    data: () => ({
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required'
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 7 &&v.length <= 10) || 'Password must have more than 7 and less than 10 characters'
      ],
      confirmpassRules: [
        v => !!v || 'Confirm Password is required'
      ],
      formCreateUser: [],
      confirmpassword: '',
      password: '',
      checkbox: false
    }),

    methods: {
      submit () {
        if (this.$refs.formCreateUser.validate() && this.password == this.confirmpassword) {
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
