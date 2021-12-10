import axios from 'axios';

let backEndAddress = "";

export default function post(parameters){
    axios.post(backEndAddress, parameters)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}