// ejercicio09.js
function sumarArreglo(arr) {
 let nicolas_ruiz1 = 0;
 for (let nicolas_ruiz2 = 0; nicolas_ruiz2 < arr.length; nicolas_ruiz2++) {
 nicolas_ruiz1 += arr[nicolas_ruiz2];
 }
 return nicolas_ruiz1;
}
let ventas = [100, 200, 300, 400, 500];
console.log("Total:", sumarArreglo(ventas));
// Salida: 1500


//Anatomía del Bucle for
//Inicialización: let nicolas_ruiz2 = 0
// Comienza en el índice 0
//Condición: nicolas_ruiz2 < arr.length
//Continúa mientras nicolas_ruiz2 sea menor que la longitud
//Incremento: nicolas_ruiz2++
//Aumenta nicolas_ruiz2 después de cada iteración
//Acumulador: nicolas_ruiz1 += arr[nicolas_ruiz2]
//Va sumando cada elemento
