const { error }= require('console');
const fs = require('fs');
const ARCHIVO ='dato.txt';
    fs.unlink(ARCHIVO,(error)=>{
    error ? console.log('no se pudo borrar el archivo'): console.log('archivo borrado correctamente');
   });