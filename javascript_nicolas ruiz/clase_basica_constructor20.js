class Autonicolas_ruiz {
  constructor(cuervoMarca, cuervoModelo) {
    this.cuervoMarca = cuervoMarca;
    this.cuervoModelo = cuervoModelo;
  }

  obtenerDescripcionnicolas_ruiz() {
    return `Marca: ${this.cuervoMarca}, Modelo: ${this.cuervoModelo}`;
  }
}

const minicolas_ruizAuto = new Autonicolas_ruiz("Toyota", "Corolla");
console.log(minicolas_ruizAuto.obtenerDescripcionnicolas_ruiz());

export default Autonicolas_ruiz;

// TIP: Las clases permiten encapsular propiedades y métodos para representar objetos con comportamiento.
