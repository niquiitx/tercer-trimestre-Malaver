const fs = require('fs');
const ARCHIVO = 'dato.txt';

fs.readFile(ARCHIVO, 'utf-8', (error, data) => {
    if (error) {
        console.log('No se pudo leer el archivo');
    } else {
        console.log('Contenido actual:', data);

        const nuevoContenido = data + '\nNueva línea agregada por Yeison';

        fs.writeFile(ARCHIVO, nuevoContenido, (err) => {
            if (err) {
                console.log('Error al escribir en el archivo');
            } else {
                console.log('Archivo editado correctamente');
            }
        });
    }
});
