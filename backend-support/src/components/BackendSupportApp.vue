<template>
	<v-content>
		<v-toolbar dark>
			<v-toolbar-title class="white--text">Backoffice Trailerflix</v-toolbar-title>
			<v-spacer></v-spacer>
		</v-toolbar>
	
		<v-container fluid>
			<form>
				<v-text-field v-model="title" :error-messages="nameErrors" label="Title" required @input="$v.name.$touch()" @blur="$v.name.$touch()"></v-text-field>
				<v-text-field v-model="sinopse" :error-messages="emailErrors" label="Sinopse" required @input="$v.email.$touch()" @blur="$v.email.$touch()"></v-text-field>
				<v-text-field v-model="year" :error-messages="yearErrors" label="Year" required @input="$v.year.$touch()" @blur="$v.year.$touch()"></v-text-field>
				<v-flex xs12 class="text-xs-center text-sm-center text-md-center text-lg-center">
					<img :src="imageUrl" height="150" v-if="imageUrl" />
					<v-text-field label="Select Image" @click='pickFile' v-model='imageName' prepend-icon='attach_file'></v-text-field>
					<input type="file" style="display: none" ref="image" accept="image/*" @change="onFilePicked" required>
				</v-flex>
	
				<v-flex xs12 class="text-xs-center text-sm-center text-md-center text-lg-center">
					<video :src="videoUrl" height="150" v-if="videoUrl" />
					<v-text-field label="Select Video" @click='pickFile' v-model='videoName' prepend-icon='attach_file'></v-text-field>
					<input type="file" style="display: none" ref="video" accept="video/*" @change="onFilePicked">
				</v-flex>
	
				<v-container fluid>
					lol
					<v-checkbox v-model="selected" label="John" value="John"></v-checkbox>
					<v-checkbox v-model="selected" label="Jacob" value="Jacob"></v-checkbox>
					<v-list-tile v-for="category in categories" :key="category.id" label="Select Categories">
						<v-list-tile-content>
							<v-checkbox :key="category.id" :label="category.name" v-model="selected[category.id]">
							</v-checkbox>
						</v-list-tile-content>
					</v-list-tile>
				</v-container>
				<v-btn v-on:click="submit()" dark>Submit</v-btn>
				<v-btn @click="clear">clear</v-btn>
			</form>
		</v-container>
	</v-content>
</template>

<script>
	import {
		getCategories,
		createVideo
	} from "@/helpers/Backend/backend.js";
	
	export default {
	
		data: () => ({
			title: '',
			year: '',
			sinopse: '',
			dialog: false,
			imageName: '',
			videoName: '',
			imageFile: '',
			categories: [],
			selected: []
		}),
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
			submit() {
				if (this.$refs.formCreateNewTrailer.validate()) {
					// Native form submission is not yet supported
					createVideo(this.name, this.password, this.email, 'Admin').then(suc => {
						console.log("registou");
						router.push('/homePage');
					}).catch(err => {
						throw err;
					})
				}
			},
			clear() {
				this.$refs.form.reset()
			}
		},
		mounted() {
			let categories = this.$store.getters.categories;
			console.log(`categories:: ${JSON.stringify(categories)}`);
			if (categories) {
				this.categories = categories;
			} else {
				this.listCategories();
			}
		}
	}
</script>
