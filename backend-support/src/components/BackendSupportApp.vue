<template>
<v-content>
 <v-toolbar dark>
            <v-toolbar-title class="white--text">Backoffice Trailerflix</v-toolbar-title>
            <v-spacer></v-spacer>
</v-toolbar>

			<v-container fluid>
  <form>
    <v-text-field
      v-model="name"
      :error-messages="nameErrors"
      label="Title"
      required
      @input="$v.name.$touch()"
      @blur="$v.name.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="email"
      :error-messages="emailErrors"
      label="Sinopse"
      required
      @input="$v.email.$touch()"
      @blur="$v.email.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="year"
      :error-messages="yearErrors"
      label="Year"
      required
      @input="$v.year.$touch()"
      @blur="$v.year.$touch()"
    ></v-text-field>
		<v-flex xs12 class="text-xs-center text-sm-center text-md-center text-lg-center">
					<img :src="imageUrl" height="150" v-if="imageUrl"/>
					<v-text-field label="Select Image" @click='pickFile' v-model='imageName' prepend-icon='attach_file'></v-text-field>
					<input
						type="file"
						style="display: none"
						ref="image"
						accept="image/*"
						@change="onFilePicked"
						required
					>
				</v-flex>

					<v-flex xs12 class="text-xs-center text-sm-center text-md-center text-lg-center">
					<video :src="videoUrl" height="150" v-if="videoUrl"/>
					<v-text-field label="Select Video" @click='pickFile' v-model='videoName' prepend-icon='attach_file'></v-text-field>
					<input
						type="file"
						style="display: none"
						ref="video"
						accept="video/*"
						@change="onFilePicked"
						required
					>
				</v-flex>

    <v-btn @click="submit">submit</v-btn>
    <v-btn @click="clear">clear</v-btn>
  </form>
			</v-container>
</v-content>
</template>

<script>
 export default {

data: () => ({
        title: "Image Upload",
        dialog: false,
		imageName: '',
		imageUrl: '',
		imageFile: ''
    }),

    methods: {
        pickFile () {
            this.$refs.image.click ()
        },
		
		onFilePicked (e) {
			const files = e.target.files
			if(files[0] !== undefined) {
				this.imageName = files[0].name
				if(this.imageName.lastIndexOf('.') <= 0) {
					return
				}
				const fr = new FileReader ()
				fr.readAsDataURL(files[0])
				fr.addEventListener('load', () => {
					this.imageUrl = fr.result
					this.imageFile = files[0] // this is an image file that can be sent to server...
				})
			} else {
				this.imageName = ''
				this.imageFile = ''
				this.imageUrl = ''
			}
		}
    }
}
  
</script>

<style>

</style>
