let año = parseInt(prompt("Ingrese un año nicolas ruiz:"));
if ((año % 4 === 0 && año % 100 !== 0) || año % 400 === 0) {
  alert(año + " es un año bisiesto.");
} else {
  alert(año + " no es bisiesto.");
}
