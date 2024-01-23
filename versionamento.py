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

# Entendendo uma função lambda:

# Sintaxe básica -> lambda argumentos: expressão
# Ex: square = lambda x: x**2 

def calcula(n):

  return lambda a : a * n

x = calcula(4) # x agora é a função e 4 é o n.

print(x(11)) # Aqui o 11 assume o valor de a