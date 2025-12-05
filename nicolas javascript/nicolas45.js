
let nicolas_ruiz42 = [
"Hacer cama",
"Comprar pan",
"Estudiar JS",
"Lavar platos"
];

console.log("Inicial:", tareas);

// splice(índice, cantidad_eliminar, nuevo_elemento)
tareas.splice(1, 1, "Pasear al perro");

console.log("Final nicolas ruiz:", tareas);
// ["Hacer cama", "Pasear al perro",
// "Estudiar JS", "Lavar platos"]
//nicolas ruiz