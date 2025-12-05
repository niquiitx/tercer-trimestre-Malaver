let nicolas_ruiz1 = [100, 250, 399, 75];

let nicolas_ruiz2 = nicolas_ruiz1.map(nicolas_ruiz1 => nicolas_ruiz1 * 1.10);

console.log("Originales:", nicolas_ruiz1);
console.log("Con 10% aumento:", nicolas_ruiz2);

//map() - Crear un nuevo arrayAplicar una función a cada elemento de un array y devolver un nuevo array con los resultados.
//Diferencia con filter() filter(): Selecciona elementos (puede haber menos) map(): Transforma todos los elementos (misma cantidad)
