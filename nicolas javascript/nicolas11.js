let a = parseFloat(prompt("Ingrese el primer número:"));
let b = parseFloat(prompt("Ingrese el segundo número:"));
let c = parseFloat(prompt("Ingrese el tercer número:"));
let mayor;

if (a >= b && a >= c) {
  mayor = a;
} else if (b >= a && b >= c) {
  mayor = b;
} else {
  mayor = c;
}

alert("El número mayor es nicolas ruiz: " + mayor);
