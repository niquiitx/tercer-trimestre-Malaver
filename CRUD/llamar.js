const { error } = require('console');
const fs = require('fs');
const ARCHIVO ='dato.txt';
    fs.readFile(ARCHIVO,'utf-8',(error, data)=>{
    error ? console.log('no se pudo leer el archivo'): console.log(data);
});