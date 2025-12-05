class ProductoAlimenticio extends Producto {
constructor(nombre, precio, cantidad, fecha) {
super(nombre, precio, cantidad);
this.fechaVencimiento = fecha;
this.categoria = "Alimenticio";
}
}

class Inventario {
constructor() {
this.productos = [];
}

agregar(producto) {
this.productos.push(producto);
}

buscarPorCategoria(categoria) {
return this.productos.filter(
p => p.categoria === categoria
);
}
}
//nicolas ruiz