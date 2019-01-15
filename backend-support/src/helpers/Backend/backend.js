import {
    baseCatalogueURL,
    baseVideoURL
} from "../general";



export function getCategories() {
    return new Promise(function (resolve, reject) {
  
      let requestUrl = baseCatalogueURL + "api/category/";
  
      let requestOptions = {
        uri: requestUrl,
        method: "GET",
        headers: {
          'Content-Type': 'application/json',
          'pragma': 'no-cache',
          'cache-control': 'no-cache',
          'jwt': localStorage.getItem('token')
        },
        //body: JSON.stringify({ "largura": largura, "comprimento": comprimento })
      }
  
      fetch(requestUrl, requestOptions).then(function (response) {
        if (response.status === 200) {
          return resolve(response.json());
        } else {
          return reject(Error("An error has occurred! Please try again."));
        }
      }, function (error) {
        return reject(error);
      });
    });
  }

  export function createTrailer(title, description, year, categoryIds, file,image) {
    console.log(`categoryIds ${(categoryIds)}`);
    console.log(`description ${(description)}`);
    return new Promise(function (resolve, reject) {
  
      let requestUrl = baseCatalogueURL + "api/catalogue/";
      
      let data = new FormData();
     
      data.append('title', title)
      data.append('year', year)
      data.append('description', description)
      data.append('category', categoryIds)
      data.append('file', file)
      data.append('image', image)
      console.log(`data ${(data.values)}`);
      let requestOptions = {
        uri: requestUrl,
        method: "POST",
        headers: {
        
          
          'pragma': 'no-cache',
          'cache-control': 'no-cache',
          'jwt': localStorage.getItem('token')
        },
        body: data
      }
  
      fetch(requestUrl, requestOptions).then(function (response) {
        if (response.status === 200) {
          console.log(`responseresponse ${JSON.stringify(response.clone().json())}`);
          return resolve(response.clone().json());
        } else {
          return reject(Error("An error has occurred! Please try again."));
        }
      }, function (error) {
        return reject(error);
      });
    });
  }

  export function addVideoTrailer(catalogue_id, path) {
    return new Promise(function (resolve, reject) {
  
      let requestUrl = baseVideoURL + "add_video";
  
      let data = new FormData();

      data.append('catalogue_id', catalogue_id)
      data.append('path', path)


      let requestOptions = {
        uri: requestUrl,
        method: "POST",
        headers: {
           
          'pragma': 'no-cache',
          'cache-control': 'no-cache',
          'jwt': localStorage.getItem('token')
        },
        body:data
      }
  
      fetch(requestUrl, requestOptions).then(function (response) {
        if (response.status === 200) {
          return resolve(response.json());
        } else {
          return reject(Error("An error has occurred! Please try again."));
        }
      }, function (error) {
        return reject(error);
      });
    });
  }