const nicolas_ruiz1 = 3.14159;
// nicolas_ruiz1 = 3.14; // ERROR!
console.log(nicolas_ruiz1); // 3.14159
//Las constantes NO pueden
//reasignarse después de
//declararse


let nicolas_ruiz2 = 10;

nicolas_ruiz2 = 20; // Válido
console.log(nicolas_ruiz2); // 20
//Las variables con let pueden
//cambiar de valor libremente

{
let temporal = 5;
const fija = 10;
console.log(temporal)
console.log(fija)
}
//Tanto let como const tienen ámbito
//de bloque (dentro de {})
