from pathlib import Path

archivo = Path("10-archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
texto.insert(0, "Hola Mundo!")
archivo.write_text("\n".join(texto), "utf-8")