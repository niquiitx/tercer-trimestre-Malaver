// =====================
//  CALCULADORA EN NODE
// =====================

// Obtenemos los argumentos enviados por consola
const operacion = process.argv[2];
const num1 = parseFloat(process.argv[3]);
const num2 = parseFloat(process.argv[4]);

// Función para realizar la operación
function calcular(op, a, b) {
    switch (op) {
        case "suma":
            return a + b;
        case "resta":
            return a - b;
        case "multiplicacion":
            return a * b;
        case "division":
            if (b === 0) return "No se puede dividir entre 0";
            return a / b;
        default:
            return "Operación no válida";
    }
}

// Mostramos resultado
console.log("Resultado:", calcular(operacion, num1, num2));
