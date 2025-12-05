// Auto.js
class Auto {
constructor(marca, modelo) {
this.marca = marca;
this.modelo = modelo;
}

obtenerDescripcion() {
return `Marca: ${this.marca}, Modelo: ${this.modelo}`;
}
}

const nicolas_ruiz46 = new Auto("Toyota", "Corolla nicolas ruiz");
console.log(miAuto.obtenerDescripcion());
// "Marca: Toyota, Modelo: Corolla"

export default Auto;
//nicolas ruiz