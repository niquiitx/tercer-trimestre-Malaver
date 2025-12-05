let nicolas_ruiz1 = prompt("Ingrese primer valor:");
let nicolas_ruiz2 = prompt("Ingrese segundo valor:");

let n1 = parseInt(nicolas_ruiz1, 10);
let n2 = parseInt(nicolas_ruiz2, 10);

if (isNaN(n1) || isNaN(n2)) {
 alert("Por favor ingrese números válidos");
} else {
 let resultado = n1 + n2;
 alert(`El resultado de ${n1} + ${n2} = ${resultado}`);
}

// Siempre valida las entradas del usuario. La función isNaN() verifica si un valor NO es un número, -
// permitiéndote detectar conversiones fallidas y proporcionar retroalimentación clara al usuario.
