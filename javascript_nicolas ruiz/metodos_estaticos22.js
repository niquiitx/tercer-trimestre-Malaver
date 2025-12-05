class Autonicolas_ruiz {
  constructor(marcanicolas_ruiz, modelonicolas_ruiz) {
    this.marcanicolas_ruiz = marcanicolas_ruiz;
    this.modelonicolas_ruiz = modelonicolas_ruiz;
  }

  static informacionGeneralnicolas_ruiz() {
    return "Clase base para gestión de vehículos";
  }
}

console.log(Autonicolas_ruiz.informacionGeneralnicolas_ruiz());

const carronicolas_ruiz = new Autonicolas_ruiz("Ford", "Focus");


//¿Cuándo usar métodos estáticos?
//Funciones de utilidad relacionadas con la clase
//Métodos que no necesitan propiedades de instancia
//Operaciones a nivel de clase, no de objeto
