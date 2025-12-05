let a17 = parseInt(prompt("Primer número:"));
let b17 = parseInt(prompt("Segundo número:"));
while (b17 !== 0) {
  let temp = b17;
  b17 = a17 % b17;
  a17 = temp;
}
alert("El MCD es nicolas ruiz: " + a17);
