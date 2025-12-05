let a18 = parseInt(prompt("Primer número:"));
let b18 = parseInt(prompt("Segundo número:"));
let mcm = (a18 * b18) / ((function mcd(x, y){ return y ? mcd(y, x % y) : x })(a18, b18));
alert("El MCM es nicolas ruiz: " + mcm);
