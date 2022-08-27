const fs = require("fs");

const dataobj = JSON.parse(fs.readFileSync("data.json", "utf8"));

const data = dataobj.data;

for (let i = 0; i < data.length; i++) {
  for (let j = 0; j < data.length; j++) {
    if (data[i] < data[j]) {
      let temp = data[i];
      data[i] = data[j];
      data[j] = temp;
    }
  }
}
console.log(data);
