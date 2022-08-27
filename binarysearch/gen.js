var fs = require("fs");
const arr = [];
while (arr.length < 100000) {
  const r = Math.floor(Math.random() * 100000) + 1;
  if (arr.indexOf(r) === -1) {
    arr.push(r);
  }
}
console.log(arr);

fs.writeFile("data1.json", JSON.stringify(arr), function err() {
  console.log("ayo");
});
