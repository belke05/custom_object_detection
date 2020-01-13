const fs = require("fs");
const puppeteer = require("puppeteer");
const request = require("request");
const path = require("path");

const makeDirectory = dirpath => {
  fs.mkdirSync(process.cwd() + dirpath, { recursive: true }, err => {
    if (err) {
      console.log(err);
    } else {
      console.log("directory made");
    }
  });
};

// to load more images
const autoScroll = async page => {
  await page.evaluate(async () => {
    await new Promise((resolve, reject) => {
      var totalHeight = 0;
      var distance = 100;
      var timer = setInterval(() => {
        var scrollHeight = document.body.scrollHeight;
        window.scrollBy(0, distance);
        totalHeight += distance;
        console.log("scroll height", scrollHeight);
        if (totalHeight >= scrollHeight) {
          clearInterval(timer);
          resolve();
        }
      }, 100);
    });
  });
};

const openpage = async searchTerm => {
  let sources = [];

  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });
  await page.goto(
    `https://www.google.com/search?biw=1030&bih=857&tbm=isch&sxsrf=ACYBGNTkdgyqXxqZ_hOdlpuSy1W9nj2mKw%3A1578834055032&sa=1&ei=hxgbXuvRAcTzkwXy36-QAQ&q=${searchTerm}&oq=${searchTerm}&gs_l=img.3..0i67l5j0l5.2480.3736..3927...0.0..0.102.664.5j2......0....1..gws-wiz-img.......35i39.cTYGIGbGfnA&ved=0ahUKEwirsYmYj_7mAhXE-aQKHfLvCxIQ4dUDCAc&uact=5`
  );

  await autoScroll(page);

  // get the links for the pictures off good quality
  const anchors = await page.$$eval(
    "div.rg_bx.rg_di.rg_el > a.rg_l",
    anchors => {
      return anchors.slice(5).map(anchor => anchor.href);
    }
  );

  for (let i = 0; i < anchors.length; i++) {
    await page.goto(anchors[i]);
    try {
      page.waitForNavigation();
      const pageTitle = await page.title();
      sources.push(pageTitle);
    } catch (err) {
      console.log(err, "element not found");
    }
  }
  sources = sources.map(
    source => {
      try {
        const match = source
          .toString()
          .match(/http.*/g)[0]
          .replace(" ", "");
        return match;
      } catch (err) {
        console.log(err);
      }
    }
    // source.replace("Google Image Result for ", "")
  );
  await browser.close();
  return sources;
};

const download = (uri, fileName, callback, directoryPath) => {
  request.head(uri, function(err, res, body) {
    try {
      if (err) {
        throw "error in the request!";
      }
      console.log("content-length:", res.headers["content-length"]);
      if (!contentIsValid(res.headers["content-type"], fileName)) {
        throw "Content is not an image!";
      }
      const output = path.join(
        __dirname,
        directoryPath,
        `${fileName}.${getFileType(res.headers["content-type"])}`
      );
      console.log("output", output);
      // creates a readstream
      request(uri)
        .pipe(fs.createWriteStream(output))
        .on("finish", callback);
    } catch (error) {
      console.log(error);
    }
  });
};

const getFileType = contentType =>
  contentType.match(/\/.*/g)[0].replace("/", "");

const contentIsValid = (contentType, fileName) => {
  if (!contentType.includes("image") || fileName.includes("html")) {
    return false;
  }
  return true;
};

exports.makeDirectory = makeDirectory;
exports.autoScroll = autoScroll;
exports.openpage = openpage;
exports.download = download;
