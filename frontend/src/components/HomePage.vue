<template>
    <div>
        <app-searchbar></app-searchbar>
        <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
                <v-flex v-for="trailer in lista_de_trailers" :key="trailer.id" xs6>
                    <app-card v-bind:trailer="trailer" v-bind:key=trailer.id></app-card>
                </v-flex>
            </v-layout>
        </v-container>
        <v-layout row justify-end>
            <v-dialog v-model="dialog" scrollable max-width="300px">
                <v-btn slot="activator" color="purple" dark>Subscribe Interests</v-btn>
                <v-card>
                    <v-card-title>Select a Category</v-card-title>
                    <v-divider></v-divider>
                    <v-list-tile v-for="category in lista_de_categorias" :key="category.id">
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
                lista_de_trailers: [],
                lista_de_categorias: [],
                categories: [{
                    id: 1,
                    name: "Comedy"
                },
                {
                    id: 2,
                    name: "Romantic"
                },
                {
                    id: 3,
                    name: "Action"
                },
                {
                    id: 4,
                    name: "Sci-Fi"
                },
                {
                    id: 5,
                    name: "Terror"
                },
                {
                    id: 6,
                    name: "Drama"
                },
                ],
                trailers: [{
                        id: 1,
                        rating: 5,
                        name: "name 1",
                        category: "action"
                    },
                    {
                        id: 2,
                        rating: 3,
                        name: "name 2",
                        category: "sci-fi"
                    },
                    {
                        id: 3,
                        rating: 2,
                        name: "name 3",
                        category: "comedy"
                    },
                    {
                        id: 4,
                        rating: 4,
                        name: "name 4",
                        category: "romance"
                    }
                ]
            }    
        },
        methods: {
            listarTrailers: function() {
                getCatalogue().then(suc => {
                    suc.data.forEach(element => {
                        this.lista_de_trailers.push(element);
                    });
                    //console.log(suc.data)
                })
                .catch(err => {
                    throw err;         
                });
            },
            listarCategorias: function() {
                getCategories().then(suc => {
                    suc.data.forEach(element => {
                        this.lista_de_categorias.push(element);
                    });
                    //console.log(suc.data)
                })
                .catch(err => { 
                    throw err; 
                   // console.log(err);
                });
            },
        },
        mounted() {
            this.listarTrailers();
            this.listarCategorias();
        }    
    }
</script>

<style>
    body {
        background: black;
    }
</style>





