function clasificarnicolas_ruiz(cuervoF) {
  if (cuervoF >= 14 && cuervoF < 32) {
    return "Temperatura baja";
  } else if (cuervoF >= 32 && cuervoF < 68) {
    return "Temperatura adecuada";
  } else if (cuervoF >= 68 && cuervoF < 96) {
    return "Temperatura alta";
  } else {
    return "Temperatura desconocida";
  }
}

console.log(clasificarnicolas_ruiz(25));
console.log(clasificarnicolas_ruiz(50));
console.log(clasificarnicolas_ruiz(85));

// TIP: Usa rangos con operadores lógicos para clasificar valores dentro de categorías específicas.
