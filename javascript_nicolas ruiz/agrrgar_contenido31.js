import fs from 'fs';

const cuervoLinea = " Nueva entrada: Verificación OK\n";

fs.appendFile('log.txt', cuervoLinea, (nicolas_ruizErr) => {
  if (nicolas_ruizErr) {
    console.error("Error:", nicolas_ruizErr);
    return;
  }
  console.log("Dato agregado (APPEND)");
});


