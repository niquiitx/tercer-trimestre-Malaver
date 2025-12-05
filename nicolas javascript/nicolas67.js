
import fs from 'fs';

const nicolas_ruiz52 =
"--- Nueva entrada: Verificación OK\n";

fs.appendFile('log.txt nicolas ruiz', nuevaLinea, (err) => {
if (err) {
console.error("Error:", err);
return;
}
console.log("Dato agregado (APPEND)");
});