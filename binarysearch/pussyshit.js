var fs = require("fs");
const arr = [];
for (let i = 0; i < 100000000; i++) {
  arr.push(i);
}
console.log(arr);

fs.writeFile(
  "data1.json",
  '{"data":' + JSON.stringify(arr) + "}",
  function err() {
    console.log("ayo");
  }
);
