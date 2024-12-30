from pathlib import Path
# import db
# import graphql
# import api
path = Path()

paths = [p for p in path.iterdir() if p.is_dir() and not p.name.startswith('.')]

# dependencias={
#     "db": db,
#     "api": api,
#     "graphql": graphql

# }



def load(p):
    paquete = __import__(str(p).replace("/","."))
    
    try:
        paquete.init()
    except:
        print("el paquete no tiene funcion init")


list(map(load,paths))