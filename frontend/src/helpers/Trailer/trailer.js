import {
    baseCatalogueURL,
    baseVideoURL
} from "../general";

export function getTrailer(trailerId) {
    return new Promise(function (resolve, reject) {
  
      let requestUrl = `${baseCatalogueURL}api/catalogue/${trailerId}/`;
  
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

export function getWatchTrailer(trailerId) {
    return new Promise(function (resolve, reject) {
  
      let requestUrl = `${baseVideoURL}videos/${trailerId}`;
     
      let requestOptions = {
        uri: requestUrl,
        method: "GET",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'pragma': 'no-cache',
          'cache-control': 'no-cache',
          'jwt': localStorage.getItem('token')
        },
      }
  
      fetch(requestUrl, requestOptions).then(function (response) {
        if (response.status === 200) {
          return resolve(response.text());
          
        } else {
          return reject(Error("An error has occurred! Please try again."));
        }
      }, function (error) {
        return reject(error);
      });
    });
  }