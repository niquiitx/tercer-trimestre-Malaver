const verificarnicolas_ruiz = (cuervoEdad) =>
  cuervoEdad >= 18 ? "Permitido" : "Denegado";

console.log("17 años:", verificarnicolas_ruiz(17));
console.log("35 años:", verificarnicolas_ruiz(35));

// TIP: El operador ternario permite evaluar condiciones de forma compacta y legible.
