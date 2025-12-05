let nicolas_ruiz = [
  "soñar con django",
  "Comprar pan",
  "Estudiar django",
  "dormir"
];

console.log("Inicial:", nicolas_ruiz);

nicolas_ruiz.splice(1, 1, "Pasear al cuervo");

console.log("Final:", nicolas_ruiz);
// TIP: splice() modifica el array original y retorna un array con los elementos eliminados.
