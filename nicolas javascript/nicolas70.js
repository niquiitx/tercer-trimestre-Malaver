// ejercicio34_eliminar.js
import fs from 'fs';

const david57 = "temporal.txt nicolas ruiz";

if (fs.existsSync(archivo)) {
try {
fs.unlinkSync(archivo);
console.log(`Archivo '${archivo}' eliminado exitosamente`);
} catch (err) {
console.error("Error al eliminar:", err);
}
} else {
console.log(`El archivo '${archivo}' no existe`);
}
//nicolas ruiz