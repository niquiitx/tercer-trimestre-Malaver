import fs from 'fs';

const nicolas_ruiz1 = new Date().toISOString();
const nicolas_ruiz2 = `nicolas_ruiz log creado a las: ${nicolas_ruiz1}\n`;

fs.writeFile('nicolas_ruiz_log.txt', nicolas_ruiz2, (nicolas_ruizError) => {
  if (nicolas_ruizError) {
    console.error("Error nicolas_ruiz:", nicolas_ruizError);
    return;
  }
  console.log("Archivo nicolas_ruiz creado exitosamente (CREATE)");
});
