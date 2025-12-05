const nicolas_ruiz1 = (cuervoBase, cuervoAltura) => {
  return (cuervoBase * cuervoAltura) / 2;
};

const nicolas_ruiz2 = (cuervoBase, cuervoAltura) =>
  (cuervoBase * cuervoAltura) / 2;

console.log("Área:", nicolas_ruiz1(8, 5));

// TIP: Puedes usar funciones flecha con return implícito para simplificar cálculos como este.
