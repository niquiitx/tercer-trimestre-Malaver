let mes = parseInt(prompt("Ingrese el número del mes (1-12) nicolas ruiz:"));
let nicolas_ruiz20;

switch (mes) {
  case 12: case 1: case 2:
    estacion = "Invierno"; break;
  case 3: case 4: case 5:
    estacion = "Primavera"; break;
  case 6: case 7: case 8:
    estacion = "Verano"; break;
  case 9: case 10: case 11:
    estacion = "Otoño"; break;
  default:
    estacion = "Mes inválido";
}
alert("Estación: " + estacion);
