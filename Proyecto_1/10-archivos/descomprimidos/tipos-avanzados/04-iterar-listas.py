mascotas= ["Loki", "Shaky", "Gordo", "Nessme", "Sasha"]



for mascota in mascotas:
    print(mascota)


for mascota in enumerate(mascotas):       #(0, 'Loki')
    print(mascota)                        #(1, 'Shaky')
                                          #(2, 'Gordo')
                                          #(3, 'Nessme')
                                          #(4, 'Sasha')


for mascota in enumerate(mascotas):       
    print(mascota[0]) 
    print(mascota[1]) 

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)