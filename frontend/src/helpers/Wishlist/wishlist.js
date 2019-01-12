import {
  base_wish_url
} from "../general";

export function addCategoriesToWishlist(categoryIds) {
    return new Promise(function (resolve, reject) {
  
      let requestUrl = base_wish_url + "api/wishlist/";
  
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
          "categoryIds": categoryIds,
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