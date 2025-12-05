import fs from 'fs';

function actualizarnicolas_ruiz(cuervoContenido) {
  fs.writeFile('log.txt', cuervoContenido, (nicolas_ruizErr) => {
    if (nicolas_ruizErr) {
      console.error("Error:", nicolas_ruizErr);
      return;
    }
    console.log("Archivo actualizado (UPDATE)");
  });
}

const cuervoActualizado =
  "Registro actualizado: " + new Date().toLocaleString() + "\n";

actualizarnicolas_ruiz(cuervoActualizado);

// TIP: writeFile sobrescribe el contenido del archivo, útil para actualizaciones completas.
