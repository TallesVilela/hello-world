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


