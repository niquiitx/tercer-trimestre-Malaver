// ejercicio08.js
let nicolas_ruiz1 = ["El Quijote", "100 Años de Soledad", "Fahrenheit 451"];
console.log("Libros iniciales:", nicolas_ruiz1.length); // 3
// Agregar al final
nicolas_ruiz1.push("Moby Dick");
console.log("Después de push:", nicolas_ruiz1.length); // 4
console.log("Libros:", nicolas_ruiz1);
// Remover del final
let nicolas_ruiz2 = nicolas_ruiz1.pop();
console.log("Libro removido:", nicolas_ruiz2); // "Moby Dick"
console.log("Libros finales:", nicolas_ruiz1.length); // 3
