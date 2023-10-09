"""
flag (bandeira) - marcar um local
is e is not = é ou não é (tipo, valor, identidade)
id = identidade


no exemplo abaixo, a variavel passou_no_if esta recebendo none, logo depois existe uma condição que diz que a variavel é true de acordo com a outra
variavel definida antes, entao no final do codigo esta sendo informado que a variavel "is None", entao isso esta incorreto pois ela foi definida
como true na primeira condição, ja na segunda parte do final do codigo esta dizendo "is not None", entao esta verdadeiro pois no começo foi definido
que o valor dele era True
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça isso")
else:
    print("Não faça isso")

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

