// ejercicio33_actualizar.js
import fs from 'fs';

function actualizarContenido(nuevoContenido) {
fs.writeFile('log.txt nicolas ruiz', nuevoContenido, (err) => {
if (err) {
console.error("Error:", err);
return;
}
console.log("Archivo actualizado (UPDATE)");
});
}

const david53 =
"Registro actualizado: " +
new Date().toLocaleString() + "\n";

actualizarContenido(contenidoActualizado);
//nicolas ruiz