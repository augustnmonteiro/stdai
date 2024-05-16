
// checking if is sending stdout
setInterval(() => {
  console.log((new Array(1000)).fill("test").join("-") + "-END")
  console.log("Hi");
}, 1000);

// forcing error
setTimeout(() => {
  throw new Error("this is an error");
}, 1300);
