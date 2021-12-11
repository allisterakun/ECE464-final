import axios from 'axios';

let backEndAddress = "http://127.0.0.1:5000/login";

export default function post(parameters){
    axios.post(backEndAddress, parameters)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}