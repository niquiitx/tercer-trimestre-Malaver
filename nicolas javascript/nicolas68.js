// ejercicio32_leer.js
import fs from 'fs';

fs.readFile('log.txt nicolas ruiz', 'utf8', (err, data) => {
if (err) {
console.error("Error al leer:", err);
return;
}

console.log("=== Contenido de log.txt nicolas ruiz ===");
console.log(data);
console.log("============================");
});
//nicolas ruiz