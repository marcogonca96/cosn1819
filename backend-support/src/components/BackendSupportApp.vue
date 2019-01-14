<template>
	<v-content>
		<v-toolbar dark>
			<v-toolbar-title class="white--text">Backoffice Trailerflix</v-toolbar-title>
			<v-spacer></v-spacer>
		</v-toolbar>
	
		<v-container fluid>
			<v-form v-model="formAddNewTrailer" ref="formAddNewTrailer" lazy-validation>
				<v-text-field v-model="title" :rules="titleErrors" label="Title" required @input="$v.title.$touch()" @blur="$v.title.$touch()"></v-text-field>
				<v-text-field v-model="description" :rules="descriptionErrors" label="Sinopse" required @input="$v.description.$touch()" @blur="$v.description.$touch()"></v-text-field>
				<v-text-field v-model="year" :rules="yearErrors" label="Year" type="number" required @input="$v.year.$touch()" @blur="$v.year.$touch()"></v-text-field>
				<v-flex xs12 class="text-xs-center text-sm-center text-md-center text-lg-center">
					<img :src="imageUrl" height="150" v-if="imageUrl" />
					<v-text-field label="Select Image" @click='pickFile' v-model='imageName' prepend-icon='attach_file'></v-text-field>
					<input type="file" style="display: none" ref="image" accept="image/*" @change="onFilePicked" required>
				</v-flex>
	
				<v-flex xs12 class="text-xs-center text-sm-center text-md-center text-lg-center">
					<video :src="videoUrl" height="150" v-if="videoUrl" />
					<v-text-field label="Select Video" @click='pickFileVideo' v-model='videoName' prepend-icon='attach_file'></v-text-field>
					<input type="file" style="display: none" ref="video" accept="video/*" @change="onFilePickedVideo">
				</v-flex>
	
				<v-container fluid>
					<h3>Select Categories</h3>
					<v-flex xs12 sm6 offset-sm3>
						<v-list-tile v-for="category in categories" :key="category.id" label="Select Categories">
							<v-list-tile-content>
								<v-checkbox :key="category.id" :label="category.name" v-model="selected[category.id]">
								</v-checkbox>
							</v-list-tile-content>
						</v-list-tile>
					</v-flex>
				</v-container>
				<v-btn v-on:click="submit()" dark>Submit</v-btn>
				<v-btn @click="clear">clear</v-btn>
			</v-form>
		</v-container>
	</v-content>
</template>

<script>
	import {
		getCategories,
		createTrailer,
		addVideoTrailer
	
	} from "@/helpers/Backend/backend.js";
	
	export default {
	
		data: () => ({
			valid: true,
			title: '',
			titleRules: [
				v => !!v || 'Title is required'
			],
			description: '',
			descriptionRules: [
				v => !!v || 'Sinopse is required'
			],
			year: '',
			yearRules: [
				v => !!v || 'Year is required',
				v => (v && v.length >= 4 && v.length < 5) || 'Year must have 4 characters'
			],
			dialog: false,
			imageName: '',
			videoName: '',
			imageFile: '',
				videoFile: '',
			imageUrl: '',
			videoURL: '',
			
			categories: [],
			selected: {},
	
		}),
		methods: {
			listCategories: function() {
				getCategories().then(suc => {
						this.categories = suc.data;
					})
					.catch(err => {
						throw err;
						console.log(err);
					})
			},
			pickFile() {
				this.$refs.image.click()
			},
			onFilePicked(e) {
				const files = e.target.files
				if (files[0] !== undefined) {
					this.imageName = files[0].name
					
					if (this.imageName.lastIndexOf('.') <= 0) {
						return
					}
					const fr = new FileReader()
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
			},
			pickFileVideo() {
				this.$refs.video.click()
			},
			onFilePickedVideo(e) {
				const files = e.target.files
				if (files[0] !== undefined) {
					this.videoName = files[0].name
					
					if (this.videoName.lastIndexOf('.') <= 0) {
						return
					}
					const fr = new FileReader()
					fr.readAsDataURL(files[0])
					fr.addEventListener('load', () => {
						this.videoUrl = fr.result
						this.videoFile = files[0] // this is an image file that can be sent to server...
					})
				} else {
					this.videoName = ''
					this.videoFile = ''
					this.videoUrl = ''
				}
			},
			clear() {
				this.$refs.form.reset()
			},
			submit() {
				let categoryIds = Object.keys(this.selected);
				console.log(`categoryIds ${categoryIds}`);
				if (this.$refs.formAddNewTrailer.validate()) {
					createTrailer(this.title, this.description, this.year, categoryIds, this.imageFile,this.imageName).then(response => {
						return addVideoTrailer(response.catalogueId, this.videoFile)
					}).then(suc => {
						console.log("finished!");
					}).catch(err => {
						throw err;
					})
				}
			}
	
		},
		mounted() {
			this.listCategories();
		}
	}
</script>
