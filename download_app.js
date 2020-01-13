const path = require("path");
const bodyParser = require("body-parser");
const {
  makeDirectory,
  autoScroll,
  openpage,
  download
} = require("./helper_functions");

const express = require("express");
const app = express();
const server = require("http").createServer(app);

// to get the post form vale
app.use(bodyParser.urlencoded({ extended: true }));
// set up the public directory otherwise the linked stylesheet wont work
app.use(express.static(path.join(__dirname, "./public")));

app.post("/search", async (req, res, next) => {
  // search/?imgTerm=banana
  const imgTerm = req.body.imgTerm;
  const directoryName = req.body.directoryName;
  console.log(directoryName);
  const directoryPath = `/images/${directoryName}`;
  const sources = await openpage(imgTerm);
  makeDirectory(directoryPath);
  console.log("a source", sources);
  for (let i = 0; i < sources.length; i++) {
    const imgSource = sources[i];
    const imgName = `${imgTerm}_${i}`;
    try {
      download(
        imgSource,
        imgName,
        function() {
          console.log("done");
        },
        directoryPath
      );
    } catch (error) {
      console.log("no download");
    }
  }
});

server.listen(process.env.PORT || 5000, () => {
  console.log(`Listening on http://localhost:${process.env.PORT || 5000}`);
});
