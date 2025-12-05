let nicolas_ruiz1 = [];

function agregarTarea(lista, tarea) {
  const nicolas_ruiz2 = [...lista, tarea];
  console.log(`Tarea agregada: "${tarea}"`);
  return nicolas_ruiz2;
}

function completarTarea(lista, indice) {
  if (indice >= 0 && indice < lista.length) {
    const nicolas_ruiz2 = lista.map((t, i) =>
      i === indice ? "7 " + t : t
    );
    console.log("Tarea marcada como completada");
    return nicolas_ruiz2;
  } else {
    console.log("Índice inválido");
    return lista;
  }
}


function obtenerEstadisticas(lista) {
  const total = lista.length;
  const completadas = lista.filter(t => t.startsWith("7")).length;
  const pendientes = total - completadas;
  return { total, completadas, pendientes };
}


function mostrarTareas(lista) {
  console.log("\n=== LISTA DE TAREAS ===");
  lista.forEach((tarea, i) => {
    console.log(`${i}. ${tarea}`);
  });
}


nicolas_ruiz1 = agregarTarea(nicolas_ruiz1, "Estudiar JavaScript");
nicolas_ruiz1 = agregarTarea(nicolas_ruiz1, "Hacer ejercicio");
nicolas_ruiz1 = agregarTarea(nicolas_ruiz1, "Preparar presentación");

mostrarTareas(nicolas_ruiz1);

nicolas_ruiz1 = completarTarea(nicolas_ruiz1, 0);

mostrarTareas(nicolas_ruiz1);

const stats = obtenerEstadisticas(nicolas_ruiz1);
console.log("\n=== ESTADÍSTICAS ===");
console.log(`Total: ${stats.total}`);
console.log(`Completadas: ${stats.completadas}`);
console.log(`Pendientes: ${stats.pendientes}`);
