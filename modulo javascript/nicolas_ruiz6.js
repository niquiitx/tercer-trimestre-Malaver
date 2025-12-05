class ruiz {
  constructor(nombre) {
    this.nombre = nombre;
  }

  saludar() {
    console.log("Hola " + this.nombre);
  }
}

let persona = new nicolas("ruiz");
persona.saludar();

