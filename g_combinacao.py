# combinação com repetição

from math import comb

def combination(a,b):
    return comb(a,b)

while True:
    try:
        a = int(input("Digite o primeiro numero da combinaçao: "))
        b = int(input("Digite o segundo numero da combinaçao: "))
        c = comb(a,b)
        print(f"O resultado da combinaçao de {a,b} é {c}")
        break
    except:
        print("Digite apenas numeros.")    