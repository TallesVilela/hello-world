print("Este aplicativo foi criado para estudos de Git")

n = range(11)

for i in n:
    print(i)


if n[10] < 10:
    print("Cuidado com os índices")




try:
    for i in n:
        print(i)
except:
    print("Esta iteração falhou")


class Carro(object):
    def FaleComigo(self):
        print("Sou um carro.")

class Fusca(Carro):
    def FaleComFusca(self):
        print("Sou um Fusca.")

x = Carro()
y = Fusca()

x.FaleComigo()
y.FaleComigo()
y.FaleComFusca()