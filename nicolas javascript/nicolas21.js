let n16 = parseInt(prompt("Cantidad de términos nicolas ruiz:"));
let a16 = 0, b16 = 1, serie = "0, 1";
for (let i = 2; i < n16; i++) {
  let c = a16 + b16;
  serie += ", " + c;
  a16 = b16;
  b16 = c;
}
alert("Serie Fibonacci: " + serie);
