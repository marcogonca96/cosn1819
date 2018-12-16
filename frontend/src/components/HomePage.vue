<template>
    <div>
        <app-searchbar></app-searchbar>
        <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
                <v-flex v-for="trailer in trailers" :key="trailer.id" xs6>
                    <app-card 
                        v-bind:trailer="trailer"
                        v-bind:categories="trailerCategoryMap[trailer.id]"
                        v-bind:key=trailer.id></app-card>
                </v-flex>
            </v-layout>
        </v-container>
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
        <app-footer></app-footer>
    </div>
</template>


<script>
    import AppSearchbar from './AppSearchbar'
    import AppCard from './AppCard'
    import AppFooter from './AppFooter'

    import { getCatalogue, getCategories } from "@/helpers/Home/home.js";

    export default {
        components: {
            AppSearchbar,
            AppCard,
            AppFooter
        },
        data() {
            return {
                trailers: [],
                categories: [],
                trailerCategoryMap: {},
                categoriesMapping: {}
              }  
        },
        methods: {
            mapByKey: function (objectArray, property) {
                return objectArray.reduce(function (acc, obj) {
                    var key = obj[property];
                    acc[key]= obj;
                    return acc;
                }, {});
            },
            mapTrailerCategories: function (trailers, categoryMapping){
                return trailers.reduce(function (acc, obj) {
                    var categoryNames = obj.category.map( catId => categoryMapping[catId].name)
                    acc[obj.id] = categoryNames
                    
                    return acc;
                }, {});
            },
            listTrailers: function() {
                getCatalogue().then(suc => {
                    console.log(`suc ${JSON.stringify(suc)}`);
                    this.trailers = suc;
                    this.trailerCategoryMap = this.mapTrailerCategories(this.trailers, this.categoriesMapping);
                })
                .catch(err => {
                    throw err;         
                });
            },
            listCategories: function() {
                getCategories().then(suc => {
                    this.categories = suc.data;
                    this.categoriesMapping = this.mapByKey(this.categories, "id")
                    // TODO: guardar em localStorage:  localStorage.categories + localStorage.categoriesMapping
                })
                .catch(err => { 
                    throw err; 
                   console.log(err);
                });
            },
        },
        mounted() {
            this.listCategories();
            this.listTrailers();
        }    
    }
</script>

<style>
    body {
        background: black;
    }
</style>





