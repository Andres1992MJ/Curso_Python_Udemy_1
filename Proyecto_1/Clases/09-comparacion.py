class Coordenadas:
    def __init__(self, lat_P, lon_P):
        self.lat_A = lat_P
        self.lon_A = lon_P

    def __eq__(self, otro):     #MEtodo magigo de igualdad
        return self.lat_A == otro.lat_A and self.lon_A == otro.lon_A
    def __lt__(self,otro):      #Metodo magico de mayor que
        return self.lat_A + self.lon_A < otro.lat_A + otro.lon_A
    def __le__(self,otro):      #Metodo magico mayot menor que o igual
        return self.lat_A + self.lon_A <= otro.lat_A + otro.lon_A


coord_1= Coordenadas(45,744)
coord_2= Coordenadas(45,744)

print(coord_1==coord_2)  #FALSE // TRUE DESPUES DE __EQ__

coord_3= Coordenadas(47,744)
coord_4= Coordenadas(45,744)

print(coord_3>coord_4)

coord_5= Coordenadas(20,130)
coord_6= Coordenadas(20,130)

print(coord_5>=coord_6)