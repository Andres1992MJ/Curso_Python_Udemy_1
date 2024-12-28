def get_product(**datos):
    print(datos)


get_product(id="03003", name="Andres", edad=32)


def get_product2(**datos):
    print(datos["name"])


get_product2(id="03003", name="Andres", edad=32)
