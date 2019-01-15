
import {
  baseUserURL
} from "../general";

export function signIn(email, password) {
  return new Promise(function (resolve, reject) {

    let requestUrl = baseUserURL + "api/login/";

    let requestOptions = {
      uri: requestUrl,
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'pragma': 'no-cache',
        'cache-control': 'no-cache'
      },
      body: JSON.stringify({
        "email": email,
        "password": password
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