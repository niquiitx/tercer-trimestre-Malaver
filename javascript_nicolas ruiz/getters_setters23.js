class Autonicolas_ruiz {
  constructor(marcanicolas_ruiz, velocidadInicialnicolas_ruiz) {
    this.marcanicolas_ruiz = marcanicolas_ruiz;
    this._velocidadnicolas_ruiz = velocidadInicialnicolas_ruiz;
  }

  set velocidadnicolas_ruiz(valornicolas_ruiz) {
    if (valornicolas_ruiz >= 0) {
      this._velocidadnicolas_ruiz = valornicolas_ruiz;
    } else {
      console.log("Error: Velocidad no puede ser negativa");
    }
  }

  get velocidadnicolas_ruiz() {
    return this._velocidadnicolas_ruiz;
  }
}


const carronicolas_ruiz = new Autonicolas_ruiz("Ford", 80);
console.log("Velocidad:", carronicolas_ruiz.velocidadnicolas_ruiz);
carronicolas_ruiz.velocidadnicolas_ruiz = 120; 
carronicolas_ruiz.velocidadnicolas_ruiz = -50; 

//Getters y Setters: Beneficios

//Encapsulación
//El guion bajo (_velocidad) es
//una convención para indicar
//que la propiedad es "privada" y
//no debe accederse
//directamente.Getters y Setters: Beneficios

//Validación
//Los setters permiten validar
//datos antes de asignarlos,
//previniendo estados inválidos
//en tus objetos.

//Sintaxis Natural
//Se acceden como propiedades
//normales (carro.velocidad)
//aunque ejecutan funciones
//internamente.
