let tipo = prompt("Convertir (1) Metros a Pies o (2) Kilogramos a Libras nicolas ruiz: ");
let valor = parseFloat(prompt("Ingrese el valor:"));
let nicolas_ruiz22;

switch (tipo) {
  case "1":
    convertido = valor * 3.281;
    alert(valor + " metros = " + convertido.toFixed(2) + " pies");
    break;
  case "2":
    convertido = valor * 2.205;
    alert(valor + " kg = " + convertido.toFixed(2) + " libras");
    break;
  default:
    alert("Opción no válida");
}
