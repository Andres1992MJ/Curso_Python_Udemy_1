mascotas= ["Loki", "Shaky", "Gordo", "Nessme", "Sasha"]

print(mascotas[0])   #Loki
print(mascotas[2])   #Gordo

mascotas[2] = "Bicho"

print(mascotas[2])      #Bicho

print(mascotas[:3])     #['Loki', 'Shaky', 'Bicho']

print(mascotas[:4])     #['Loki', 'Shaky', 'Bicho', 'Nessme']

print(mascotas[2:4])    #['Bicho', 'Nessme']

print(mascotas[-2])     #Nessme

print(mascotas[::2])    #['Loki', 'Bicho', 'Sasha'] salta de tanto en tanto

print(mascotas[1::2])   #['Shaky', 'Nessme']

rango=list(range(31))  

print(rango[::2])  #Pares
print(rango[1:16:2]) #impares