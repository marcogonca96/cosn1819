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
            <v-badge overlap>
              <span slot="badge">3</span>
              <v-avatar color="purple red--after">
                <v-icon dark>notifications</v-icon>
              </v-avatar>
            </v-badge>
            <v-avatar color="indigo">
              <v-icon dark>account_circle</v-icon>
            </v-avatar>
          </v-toolbar>
        </div>
      </v-layout>
    </v-container>
  </v-card>
</template>
