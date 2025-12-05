let nicolas_ruiz2 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

function imprimirnicolas_ruiz(cuervo) {
  for (let nicolas_ruiz2 = 0; nicolas_ruiz2 < cuervo.length; nicolas_ruiz2++) {
    for (let cuervoIndex = 0; cuervoIndex < cuervo[nicolas_ruiz2].length; cuervoIndex++) {
      console.log(`[${nicolas_ruiz2}][${cuervoIndex}] = ${cuervo[nicolas_ruiz2][cuervoIndex]}`);
    }
  }
}

imprimirnicolas_ruiz(nicolas_ruiz2);
