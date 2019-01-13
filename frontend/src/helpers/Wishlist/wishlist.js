import {
  baseWishURL
} from "../general";

export function addCategoriesToWishlist(categoryIds) {
    return new Promise(function (resolve, reject) {
  
      let requestUrl = baseWishURL + "api/wishlist/";
  
      let requestOptions = {
        uri: requestUrl,
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
          'pragma': 'no-cache',
          'cache-control': 'no-cache',
          'jwt': localStorage.getItem('token')
        },
        body: JSON.stringify({
          "categories": categoryIds,
        })
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