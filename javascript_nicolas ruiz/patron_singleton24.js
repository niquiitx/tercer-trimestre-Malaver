class Autonicolas_ruiz {
  constructor(marcanicolas_ruiz, velocidadInicialnicolas_ruiz) {
    this.marcanicolas_ruiz = marcanicolas_ruiz;
    this._velocidadnicolas_ruiz = velocidadInicialnicolas_ruiz;
  }

  set velocidad(valor) {
    if (valor >= 0) {
      this._velocidadnicolas_ruiz = valor;
    } else {
      console.log("Error: Velocidad no puede ser negativa");
    }
  }

  get velocidad() {
    return this._velocidadnicolas_ruiz;
  }
}

const carronicolas_ruiz = new Autonicolas_ruiz("Ford", 80);

console.log("Velocidad:", carronicolas_ruiz.velocidad);
carronicolas_ruiz.velocidad = 120;
console.log("Velocidad actualizada:", carronicolas_ruiz.velocidad);
carronicolas_ruiz.velocidad = -50;
