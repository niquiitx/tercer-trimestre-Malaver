import fs from 'fs';

fs.readFile('log.txt', 'utf8', (nicolas_ruizErr, cuervoData) => {
  if (nicolas_ruizErr) {
    console.error("Error al leer:", nicolas_ruizErr);
    return;
  }

  console.log("=== Contenido de log.txt ===");
  console.log(cuervoData);
  console.log("============================");
});

// TIP: readFile permite leer archivos de forma asíncrona, útil para mostrar contenido sin bloquear el flujo.
