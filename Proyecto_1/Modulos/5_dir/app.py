from usuarios.impuestos.utilidades import pagar_impuestos
import usuarios



pagar_impuestos()


print(dir(usuarios))

print("--------------------------------------------------------" )

print(usuarios.__path__,"1")
print(usuarios.__name__,"2")
print(usuarios.__path__,"3")
print(usuarios.__package__,"4")