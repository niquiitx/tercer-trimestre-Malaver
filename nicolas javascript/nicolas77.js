// app.js
import fs from 'fs';
import { Estudiante, RegistroEstudiantes } from './Estudiante.js';

const david65 = new RegistroEstudiantes();

// Agregar estudiantes
registro.agregar(new Estudiante("nicolas ruiz", [85, 90, 88]));
registro.agregar(new Estudiante("samu", [78, 82, 80]));
registro.agregar(new Estudiante("DAVID", [92, 95, 91]));

// Mostrar promedio general
console.log("Promedio general del curso:",
registro.promedioGeneral());

// Guardar en archivo JSON
fs.writeFile(
'estudiantes.json',
registro.aJSON(),
(err) => {
if (err) {
console.error("Error al guardar:", err);
return;
}
console.log("Datos guardados exitosamente en estudiantes.json");
}
);

// Cargar desde archivo (ejemplo)
fs.readFile('estudiantes.json', 'utf8', (err, data) => {
if (err) {
console.log("Archivo no existe aún");
return;
}

const nicolas_ruiz66 = JSON.parse(data);
console.log("\nDatos cargados desde archivo:");
console.log(datosEstudiantes);
});
//nicolas ruiz