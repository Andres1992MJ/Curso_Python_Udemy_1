mascotas= ["Loki", "Shaky", "Gordo", "Nessme", "Sasha","Nessme","Shaky"]

mascotas.insert(1, "Venus")

print(mascotas, "Insert_Agrega el segundo valor en el indice indicado y corre el resto a la derecha")

mascotas.append("Kaiser")

print(mascotas, "Append_Agrega el termino dentro del ()al final")

mascotas.remove("Nessme")

print(mascotas, "Remove_Elimina el primer elemento que coincida con el termino dentro del ()")

mascotas.pop()

print(mascotas, "POP_elimina el ultimo")

mascotas.pop(3)

print(mascotas, "POP_VALOR_elimina el valor en el indice indicado")

del mascotas[1]

print(mascotas, "DEL_elimina el valor en el indice indicado")

mascotas.clear()

print(mascotas, "CLEAR_elimina todo el contenido")
