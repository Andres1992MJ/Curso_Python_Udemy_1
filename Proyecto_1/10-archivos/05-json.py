#Json: significa JavaScript, Object, Notation

import json
from pathlib import Path

#Escribir un json

productos=[
    {"id": 1, "name": "SkateBoard"},
    {"id": 2, "name": "Bicicleta"},
    {"id": 3, "name": "Patines"},
    {"id": 4, "name": "Balon"},
    {"id": 5, "name": "Surfboard"}
]

data = json.dumps(productos)

Path("10-archivos/archivo_json_1.json").write_text(data)


#LEER un Json

data = Path("10-archivos/archivo_json_2.json").read_text(encoding="utf-8")
productos_1= json.loads(data)
print(productos_1)

print("-----------------Modificacion-------------------------")

#Escribir o modificar un Json

productos_1[0]["name"] = "Pantalla"
print(productos_1[0]["name"])
Path("10-archivos/archivo_json_2.json").write_text(json.dumps(productos_1))

