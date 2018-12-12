import {
    base_user_url
} from "../general";

export function createUser(username, password, email, level) {
    return new Promise(function (resolve, reject) {
  
      let requestUrl = base_user_url + "api/user/";
  
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
          "username": username,
          "password": password,
          "email": email,
          "level": level
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