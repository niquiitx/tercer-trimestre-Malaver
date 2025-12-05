const fs=require('fs');
const ARCHIBO="dato.txt";

fs.writeFileSync(ARCHIBO,"este es mi rpimer comit",(err)=>err?console.error(err):consule.log("archivo creado"));