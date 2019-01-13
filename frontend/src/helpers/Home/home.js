import {
    baseCatalogueURL
} from "../general";

export function getCatalogue() {
    return new Promise(function (resolve, reject) {
  
      let requestUrl = baseCatalogueURL + "api/catalogue/";
  
      let requestOptions = {
        uri: requestUrl,
        method: "GET",
        headers: {
          'Content-Type': 'application/json',
          'pragma': 'no-cache',
          'cache-control': 'no-cache',
          'jwt': localStorage.getItem('token')
        },
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