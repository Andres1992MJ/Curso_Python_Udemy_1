class Lista(list):
    def preapend(self,item):
        self.insert(0,item)


lista_1=Lista([2,3,4])

lista_1.append(5)

lista_1.preapend(0)

print(lista_1)