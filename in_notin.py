"""
iteravél = caminha pelo codigo todo
strings são iteraveis
0 1 2 3 4 5 
O t á v i o 
-6 -5 -4 -3 -2 -1 
"""
nome='William'
print(nome[0])
print(nome[-7])
print(10*"=-", "=", sep='')
print("ll" in nome)
print("liam" not in nome)

nome1 = input("Digite um nome: ")

if nome1 in nome:
    print(f"{nome1} está em {nome}")
else:
    print(f"{nome1} não está em {nome}")