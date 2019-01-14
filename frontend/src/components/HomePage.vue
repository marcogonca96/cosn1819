<template>
    <div>
        <app-searchbar></app-searchbar>
        <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
                <v-flex v-for="trailer in trailers" :key="trailer.id" xs6>
                    <app-card v-bind:trailer="trailer" v-bind:categories="trailerCategoryMap[trailer.id]" v-bind:key=trailer.id></app-card>
                </v-flex>
            </v-layout>
        </v-container>

        <app-footer></app-footer>
    </div>
</template>


<script>
    import AppSearchbar from './AppSearchbar'
    import AppCard from './AppCard'
    import AppFooter from './AppFooter'
    
    import {
        getCatalogue,
        getCategories
    } from "@/helpers/Home/home.js";
    
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
            mapByKey: function(objectArray, property) {
                return objectArray.reduce(function(acc, obj) {
                    var key = obj[property];
                    acc[key] = obj;
                    return acc;
                }, {});
            },
            mapTrailerCategories: function(trailers, categoryMapping) {
                return trailers.reduce(function(acc, obj) {
                    var categoryNames = obj.category.map(catId => categoryMapping[catId].name)
                    acc[obj.id] = categoryNames
    
                    return acc;
                }, {});
            },
            listTrailers: function() {
                getCatalogue().then(suc => {
                    console.log(`SUC ${JSON.stringify(suc)}`);
                    this.trailers = suc.data;
                    this.trailerCategoryMap = this.mapTrailerCategories(this.trailers, this.categoriesMapping);
                    console.log(`this.trailerCategoryMap ${this.trailerCategoryMap}`);
                })
                .catch(err => {
                    console.log(`ERROR: ${err}`);
                    throw err;
                });
            },
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
                    });
            },
        },
        mounted() {
            
            let categories = this.$store.getters.categories;
            let categoriesMapping = this.$store.getters.categoriesMapping;

            console.log(`this.$store.getters.categories =>  ${JSON.stringify(categories)}`);
            console.log(`this.$store.getters.categoriesMapping =>  ${JSON.stringify(categoriesMapping)}`);

            if (categories && categoriesMapping) {
                this.listCategories = categories;
                this.categoriesMapping = categoriesMapping;
            } else {
                this.listCategories();
            }
            this.listTrailers();
        },
    }
</script>

<style>
    body {
        background: black;
    }
</style>





