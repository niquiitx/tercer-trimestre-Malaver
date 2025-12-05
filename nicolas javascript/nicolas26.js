// Calculadora con estructura switch
let num1 = parseFloat(prompt("Ingrese el primer número nicolas ruiz:"));
let nicolas_ruiz18 = prompt("Ingrese el operador (+, -, *, /):");
let num2 = parseFloat(prompt("Ingrese el segundo número:"));
let nicolas_ruiz6;

switch (operador) {
  case "+":
    resultado = num1 + num2;
    break;
  case "-":
    resultado = num1 - num2;
    break;
  case "*":
    resultado = num1 * num2;
    break;
  case "/":
    resultado = num2 !== 0 ? num1 / num2 : "Error: División por cero";
    break;
  default:
    resultado = "Operador inválido";
}
alert("Resultado: " + resultado);
