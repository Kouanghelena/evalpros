console.log("Frontend connecté ✔");

fetch("http://192.168.1.139:8000/docs")
  .then(res => res.text())
  .then(data => console.log("API OK"));
