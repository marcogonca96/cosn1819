<template>
    <div>
        <app-searchbar></app-searchbar>
        <div class="text-xs-center" style="margin-top:6%;margin-left:15%;margin-right:15%;margin-bottom:10%">
            <v-layout row child-flex wrap style="margin-top:3%">
                <router-link to="/homePage">
                    <v-btn icon class="hidden-xs-only">
                        <v-icon>arrow_back</v-icon>
                    </v-btn>
                </router-link>
                <h1 style="color:white; text-align:left"> Trailer {{ trailer.title }} </h1>
            </v-layout>
            <v-layout row child-flex wrap style="margin-top:3%">
                <div class="col-4">
                    <h2 style="color:white"> Categories: {{ this.categoriesList }} </h2>
                </div>
                <div class="col-4">
                    <h3 style="color:white"> Year {{ trailer.year }} </h3>
                </div>
            </v-layout>
            <br>
    
            <iframe id="ytplayer" type="text/html" width="800" height="400" :src="videoURL" frameborder="0" allowfullscreen></iframe>
            <h2 style="color:white; text-align: left"> Sinopse </h2>
            <br>
            <p style="color:white; text-align: left">{{ trailer.description }}</p>
            <v-divider></v-divider>
            <h3 style="color:white, margin-top:3%"> Rate your trailer </h3>
            <v-rating v-model="rating" background-color="white" color="yellow accent-4" dense half-increments hover size="18"></v-rating>
        </div>
    
        <app-footer></app-footer>
    </div>
</template>

<script>
    import AppFooter from './AppFooter'
    import AppSearchbar from './AppSearchbar'
    import {
        getTrailer
    } from "@/helpers/Trailer/trailer.js";
    import {
        getWatchTrailer
    } from "@/helpers/Trailer/trailer.js";
    import {
      baseVideoURL
    } from "../helpers/general.js";
    
    export default {
        components: {
            AppSearchbar,
            AppFooter
        },
        data: () => ({
            rating: 4.3,
            trailer: null,
            videoURL: null,
            watchTrailer: null,
            categoryNames: []
        }),
        created() {
            console.log(`this.$route.params ${JSON.stringify(this.$route.params)}`);
            this.trailerID = this.$route.params.trailerID;
            this.categoriesMapping = this.$store.getters.categoriesMapping || {};
        },
        methods: {
            fetchTrailer: function() {
                getTrailer(this.trailerID).then(suc => {
                        this.trailer = suc.data;
                        console.log(`sucsucsuc ${JSON.stringify(this.trailer)}`);
                        this.videoURL = `${baseVideoURL}videos/${this.trailer.id}`;
                        console.log(`trailer ${JSON.stringify(this.trailer)}`);
                        
                        this.categoryNames = this.trailer.category.map(catId => this.categoriesMapping[catId].name);
                        // eslint-disable-next-line
                       
                    })
                    .catch(err => {
                        throw err;
                    });
            },
            fetchWatchTrailer: function() {
                getWatchTrailer(this.trailerID).then(watchTrailer => {
                        this.watchTrailer = watchTrailer;
                        console.log(`watchTrailer:: ${JSON.stringify(watchTrailer)}`);
                    })
                    .catch(err => {
                        throw err;
                    });
            },
        },
        mounted() {
            this.fetchTrailer();
            this.fetchWatchTrailer();
        },
        computed: {
            categoriesList: function() {
                return this.categoryNames.join(", ")
            }
        }
    }
</script>
