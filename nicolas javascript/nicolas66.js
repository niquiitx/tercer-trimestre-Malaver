
import fs from 'fs';

const fecha = new Date().toISOString();
const david51 = `Log creado: ${fecha}\n`;

fs.writeFile('log.txt nicolas ruiz', contenido, (err) => {
if (err) {
console.error("Error:", err);
return;
}
console.log("Archivo creado exitosamente (CREATE)");
});
//nicolas ruiz