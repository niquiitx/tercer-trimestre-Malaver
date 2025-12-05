// Solicita el valor de la temperatura y lo convierte a flotante
let nicolas_ruiz54 = parseFloat(prompt("Ingrese la temperatura nicolas ruiz:"));
// Solicita el tipo de conversión deseada
let david55 = prompt("¿Desea convertir a Fahrenheit (F) o Celsius (C)?").toUpperCase();
let nicolas_ruiz56; // Declara la variable para el resultado
// Verifica si la temperatura es un número válido
if (isNaN(temperatura)) {
alert("Por favor, ingrese una temperatura válida.");
} else {
// Condición para convertir a Fahrenheit
if (tipoConversion === 'F') {
resultadoConversion = (temperatura * 9/5) + 32; // Fórmula C a F
alert(temperatura + "°C es " + resultadoConversion.toFixed(2) + "°F.");
}
// Condición para convertir a Celsius
else if (tipoConversion === 'C') {
resultadoConversion = (temperatura - 32) * 5/9; // Fórmula F a C
alert(temperatura + "°F es " + resultadoConversion.toFixed(2) + "°C.");
}
// Mensaje para tipo de conversión inválido
else {
alert("Tipo de conversión inválido. Por favor, ingrese 'F' o 'C'.");
}
}