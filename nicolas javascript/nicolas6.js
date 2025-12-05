// Solicita al usuario su edad y la convierte a número entero
let edad = parseInt(prompt("Ingrese su edad nicolas ruiz:"));
// Verifica si la edad es un número válido
if (isNaN(edad)) {
alert("Por favor, ingrese una edad válida (número).");
} else if (edad >= 18) { // Condición para verificar si es mayor de edad
alert("Usted es mayor de edad."); // Mensaje para mayores de 18
} else {
alert("Usted es menor de edad."); // Mensaje para menores de 18
}