class nicolas_ruizDireccion {
  constructor(nicolas_ruizCalle, nicolas_ruizCodigoPostal) {
    this.nicolas_ruizCalle = nicolas_ruizCalle;
    this.nicolas_ruizCodigoPostal = nicolas_ruizCodigoPostal;
  }
}

class nicolas_ruizCliente {
  constructor(nicolas_ruizNombre, nicolas_ruizDireccion) {
    this.nicolas_ruizNombre = nicolas_ruizNombre;
    this.nicolas_ruizDireccion = nicolas_ruizDireccion;
  }

  mostrarnicolas_ruizUbicacion() {
    console.log(`${this.nicolas_ruizNombre} vive en:
${this.nicolas_ruizDireccion.nicolas_ruizCalle},
CP ${this.nicolas_ruizDireccion.nicolas_ruizCodigoPostal}`);
  }
}

const nicolas_ruiz1 = new nicolas_ruizDireccion(
  "Calle de la Victoria 789", "11011"
);
const nicolas_ruiz2 = new nicolas_ruizCliente("nicolas_ruiz Gómez", nicolas_ruiz1);
nicolas_ruiz2.mostrarnicolas_ruizUbicacion();
