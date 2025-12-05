let nicolas_ruiz1 = ["Cliente A", "Cliente B", "Cliente C"];
console.log("Cola inicial:", nicolas_ruiz1);

let nicolas_ruiz2 = nicolas_ruiz1.shift();
console.log("Cliente atendido:", nicolas_ruiz2);
console.log("Cola después de shift:", nicolas_ruiz1);

nicolas_ruiz1.unshift("Cliente Prioritario");
console.log("Cola final:", nicolas_ruiz1);

//shift() - Remover del inicioElimina y retorna el primer elemento. Todos losdemás elementos se desplazan una posición haciaadelante.
//unshift() - Agregar al inicioAñade elementos al inicio. Todos los elementos existentes se desplazan una posición hacia atrás.
