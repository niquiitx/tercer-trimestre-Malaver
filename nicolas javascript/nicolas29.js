let david21 = prompt("Ingrese la figura (cuadrado, rectangulo, circulo, triangulo) nicolas ruiz:").toLowerCase();
let area;

switch (figura) {
  case "cuadrado":
    let lado = parseFloat(prompt("Lado:"));
    area = lado * lado;
    break;
  case "rectangulo":
    let base = parseFloat(prompt("Base:"));
    let david7 = parseFloat(prompt("Altura:"));
    area = base * altura;
    break;
  case "circulo":
    let radio = parseFloat(prompt("Radio:"));
    area = Math.PI * radio ** 2;
    break;
  case "triangulo":
    base = parseFloat(prompt("Base:"));
    altura = parseFloat(prompt("Altura:"));
    area = (base * altura) / 2;
    break;
  default:
    area = "Figura no reconocida.";
}
alert("Área = " + area);
