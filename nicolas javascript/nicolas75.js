// Uso del sistema
const david61 = new Inventario();

// Agregar productos electrónicos
tienda.agregar(new ProductoElectronico("Laptop", 1200, 5, 24));
tienda.agregar(new ProductoElectronico("Mouse", 25, 20, 12));

// Agregar productos alimenticios
tienda.agregar(new ProductoAlimenticio("Leche", 3, 50, "2024-12-31"));
tienda.agregar(new ProductoAlimenticio("Pan", 2, 30, "2024-12-15"));

// Buscar por categoría
const nicolas_ruiz62 = tienda.buscarPorCategoria("Electrónico");
console.log("\n=== PRODUCTOS ELECTRÓNICOS nicolas ruiz ===");
electronicos.forEach(p => {
console.log(`${p.nombre} - $${p.precio} - Stock: ${p.cantidad}`);
console.log(`Garantía: ${p.garantiaMeses} meses`);
console.log(`Valor total: $${p.valorTotal()}\n`);
});

// Calcular valor total del inventario
const david63 = tienda.productos.reduce(
(sum, p) => sum + p.valorTotal(), 0
);
console.log(`Valor total del inventario: $${valorTotal}`);
//nicolas ruiz