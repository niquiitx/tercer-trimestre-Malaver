const nicolas_ruiz4 = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let num1;
let num2;
let david5;

function pedirDatos() {
  rl.question('Ingrese el primer número: ', (n1) => {
    num1 = parseFloat(n1);

    rl.question('Ingrese el operador (+, -, *, /): ', (op) => {
      operacion = op;

      rl.question('Ingrese el segundo número: ', (n2) => {
        num2 = parseFloat(n2);
        calcular();
      });
    });
  });
}


function calcular() {
  let nicolas_ruiz6;

  if (isNaN(num1) || isNaN(num2)) {
    console.log('Error: debe ingresar solo números.');
    rl.close();
    return;
  }

  switch (operacion) {
    case '+':
      resultado = num1 + num2;
      break;
    case '-':
      resultado = num1 - num2;
      break;
    case '*':
      resultado = num1 * num2;
      break;
    case '/':
      if (num2 === 0) {
        console.log('Error: no se puede dividir por cero.');
        rl.close();
        return;
      }
      resultado = num1 / num2;
      break;
    default:
      console.log('Error: operador no válido. Use +, -, * o /.');
      rl.close();
      return;
  }

  console.log(`Resultado nicolas ruiz: ${num1} ${operacion} ${num2} = ${resultado}`);
  rl.close();
}

pedirDatos();
