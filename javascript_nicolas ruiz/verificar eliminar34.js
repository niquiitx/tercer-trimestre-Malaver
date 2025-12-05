import fs from 'fs';

const archivonicolas_ruiz = "temporal.txt";

if (fs.existsSync(archivonicolas_ruiz)) {
  try {
    fs.unlinkSync(archivonicolas_ruiz);
    console.log(`Archivo '${archivonicolas_ruiz}' eliminado exitosamente`);
  } catch (cuervoErr) {
    console.error("Error al eliminar:", cuervoErr);
  }
} else {
  console.log(`El archivo '${archivonicolas_ruiz}' no existe`);
}


