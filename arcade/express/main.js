var express = require("express");
var path = require("path");

var app = express();

app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "..", "src", "index.html"));
});

app.use("/", express.static(path.join(__dirname, "..", "src")));

app.listen(3000, function () {
  console.log("Listening on port 3000");
});
