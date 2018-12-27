<template>
    <v-card flat>
        <v-container fluid>
            <v-layout row child-flex wrap>
                <div>
                    <v-toolbar>
                        <v-toolbar-title>Search</v-toolbar-title>
                        <v-spacer></v-spacer>
                        <v-btn icon class="hidden-xs-only">
                            <v-icon>search</v-icon>
                        </v-btn>
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
                                            <v-checkbox value="category.name" :key="category.id" :label="category.name" v-model="selected">
                                            </v-checkbox>
                                        </v-list-tile-content>
                                    </v-list-tile>
                                    <v-divider></v-divider>
                                    <v-card-actions>
                                        <v-btn color="purple" dark flat @click="dialog = true" to="/homePage">Close</v-btn>
                                        <v-btn color="purple" dark flat @click="dialog = false">Save</v-btn>
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
    
    export default {
        data() {
            return {
    
                categories: [],
    
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

