<template>
    <v-card flat>
        <v-container fluid>
            <v-layout row child-flex wrap>
                <div 
  
>
                    <v-toolbar>     
   <v-spacer class="hidden-xs-only"></v-spacer>
                        <v-text-field
         dark
         solo
 style="
    width: 700px; margin-top: 0px;"
         prepend-icon="search"
         placeholder="Type Search...">
      </v-text-field>
                        <v-spacer></v-spacer>
                        
                    </v-toolbar>
                </div>
                <div style="flex-basis: 5%">
                    <v-toolbar dark>
                        <v-spacer></v-spacer>
                        <v-layout row justify-end>
                            <v-dialog v-model="dialog" scrollable max-width="300px">
                                <v-btn slot="activator" color="purple" dark>Subscribe Interests</v-btn>
                                <v-card>
                                    <v-card-title>Select a Category</v-card-title>
                                    <v-divider></v-divider>
                                    <v-list-tile v-for="category in categories" :key="category.id">
                                        <v-list-tile-content>
                                            <v-checkbox :key="category.id" :label="category.name" v-model="selected[category.id]">
                                            </v-checkbox>
                                        </v-list-tile-content>
                                    </v-list-tile>
                                    <v-divider></v-divider>
                                    <v-card-actions>
                                        <router-link to="/homePage">
                                        <v-btn color="purple" dark flat @click="dialog = false" >Close</v-btn>
                                         </router-link>
                                        <v-btn color="purple" dark flat v-on:click="save()">Save</v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-dialog>
                        </v-layout>
                        <v-badge overlap>
                            <span slot="badge">3</span>
                            <v-avatar color="purple red--after">
                                <v-icon dark>notifications</v-icon>
                            </v-avatar>
                        </v-badge>
                        <v-btn fab dark color="indigo" v-on:click="logout()" @logout="logout">
                            <v-icon dark>account_circle</v-icon>
                        </v-btn>
                    </v-toolbar>
                </div>
            </v-layout>
        </v-container>
    </v-card>
</template>

<script>
    import {
        getCategories
    } from "@/helpers/Home/home.js";
      import {
        addCategoriesToWishlist
    } from "@/helpers/Wishlist/wishlist.js";
    import router from '../router/index'

    export default {
        data() {
            return {
                categories: [],
                selected: {},
                dialog: false
            }
        },
        methods: {
            listCategories: function() {
                getCategories().then(suc => {
                        this.categories = suc.data;
                        this.categoriesMapping = this.mapByKey(this.categories, "id");
                        this.$store.dispatch('setCategories', {
                            'categories': this.categories,
                            'categoriesMapping': this.categoriesMapping
                        });
                    })
                    .catch(err => {
                        throw err;
                        console.log(err);
                    })
            },
            logout: function() {
                console.log("exit");
                this.$store.commit("logout");
            },
            save() { 
                console.log(`selected: ${JSON.stringify(this.selected)}`);
                let categoryIds = Object.keys(this.selected);
                console.log(`categoryIds ${categoryIds}`);   
                addCategoriesToWishlist(categoryIds).then(suc => {
                    
                    console.log("Wishes created!");
                    this.dialog = false;
                }).catch(err => {
                    throw err;
                })
            }
        },
        mounted() {  
            let categories = this.$store.getters.categories;
    
            if (categories) {
                this.categories = categories;
            } else {
                this.listCategories();
            }
        }
    }
</script>

