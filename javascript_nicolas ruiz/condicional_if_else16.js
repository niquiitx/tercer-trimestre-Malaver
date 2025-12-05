function esMayornicolas_ruiz(cuervoEdad) {
  if (cuervoEdad >= 18) {
    return true;
  } else {
    return false;
  }
}

function esMayornicolas_ruizSimple(cuervoEdad) {
  return cuervoEdad >= 18;
}

console.log("Edad 20:", esMayornicolas_ruiz(20));
console.log("Edad 16:", esMayornicolas_ruiz(16));

// TIP: Puedes simplificar condiciones booleanas retornando directamente la comparación.
