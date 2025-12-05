// Composición.js
class Direccion {
constructor(calle, codigoPostal) {
this.calle = calle;
this.codigoPostal = codigoPostal;
}
}

class Cliente {
constructor(nombre, direccion) {
this.nombre = nombre;
this.direccion = direccion;
}

mostrarUbicacion() {
console.log(`${this.nombre} vive en:
${this.direccion.calle},
CP ${this.direccion.codigoPostal}`);
}
}

const david47 = new Direccion(
"Avenida Central 456", "10101"
);
const juan = new Cliente("nicolas ruiz", miDireccion);
juan.mostrarUbicacion();
//nicolas ruiz