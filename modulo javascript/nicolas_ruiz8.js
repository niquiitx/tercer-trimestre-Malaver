try {
  throw new Error("Algo salió mal, ruiz");
} catch (e) {
  console.log("Error capturado:", e.message);
}

