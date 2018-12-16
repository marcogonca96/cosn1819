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
            <h1 style="color:white; text-align:left"> Trailer {{ trailer.title }}  </h1>
             </v-layout>
            <v-layout row child-flex wrap style="margin-top:3%">
                <div class="col-4">
                    <h2 style="color:white"> Category 1 </h2>
                </div>
                <div class="col-4">
                    <h3 style="color:white"> Year {{ trailer.year }} </h3>
                </div>
            </v-layout>
            <br>
            <iframe id="ytplayer" type="text/html" width="640" height="360" src="https://www.youtube.com/embed/Bf6D-i8YpHg" frameborder="0" allowfullscreen></iframe>
    
    
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
    import { getTrailer } from "@/helpers/Trailer/trailer.js";
    
    export default {
        components: {
            AppSearchbar,
            AppFooter
        },
        data: () => ({
            rating: 4.3,
            trailer: null
        }),
        created () {
            this.trailerID = this.$route.params.trailerID;
        },
         methods: {
            fetchTrailer: function() {
                getTrailer(this.trailerID).then( trailer => {
                    this.trailer = trailer;
                    // eslint-disable-next-line
                    console.log(`trailer:: ${JSON.stringify(trailer)}`);
                })
                .catch(err => {
                    throw err;         
                });
            },       
        },
        mounted() {
            this.fetchTrailer();
        }       
    }
</script>
