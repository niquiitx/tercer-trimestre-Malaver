class Auto {
  constructor(marcanicolas_ruiz, modelonicolas_ruiz) {
    this.marcanicolas_ruiz = marcanicolas_ruiz;
    this.modelonicolas_ruiz = modelonicolas_ruiz;
  }

  obtenerDescripcion() {
    return `Marca: ${this.marcanicolas_ruiz}, Modelo: ${this.modelonicolas_ruiz}`;
  }
}

class VehiculoElectrico extends Auto {
  constructor(marcanicolas_ruiz, modelonicolas_ruiz, autonomianicolas_ruiz) {
    super(marcanicolas_ruiz, modelonicolas_ruiz);
    this.autonomiaBaterianicolas_ruiz = autonomianicolas_ruiz;
  }

  mostrarInfo() {
    return `${super.obtenerDescripcion()}, Autonomía: ${this.autonomiaBaterianicolas_ruiz} km`;
  }
}

const teslanicolas_ruiz = new VehiculoElectrico("Tesla", "Model 3", 500);
console.log(teslanicolas_ruiz.mostrarInfo());
