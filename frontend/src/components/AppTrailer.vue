<template>
    <div>
        <app-searchbar></app-searchbar>
        <div class="text-xs-center" style="margin-top:6%;margin-left:15%;margin-right:15%;margin-bottom:10%">
            <v-layout row child-flex wrap style="margin-top:3%">
            <h1 style="color:white; text-align:right"> Trailer 1 </h1>
            <router-link to="/homePage">
             <v-btn icon class="hidden-xs-only">
              <v-icon>arrow_back</v-icon>
            </v-btn>
            </router-link>
             </v-layout>
            <v-layout row child-flex wrap style="margin-top:3%">
                <div class="col-4">
                    <h2 style="color:white"> Category 1 </h2>
                </div>
                <div class="col-4">
                    <h3 style="color:white"> Year 1 </h3>
                </div>
            </v-layout>
            <br>
            <iframe id="ytplayer" type="text/html" width="640" height="360" src="https://www.youtube.com/embed/Bf6D-i8YpHg" frameborder="0" allowfullscreen></iframe>
    
    
            <h2 style="color:white; text-align: left"> Sinopse 1 </h2>
            <br>
            <p style="color:white; text-align: left">All happy</p>
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
    export default {
        components: {
             AppSearchbar,
            AppFooter
        },
        data: () => ({
            rating: 4.3
        })
    }
</script>
