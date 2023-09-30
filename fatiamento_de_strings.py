"""
fatiamento de strings
012345678
Olá mundo
-987654321
fatiameneto [i:f:p] [::]
Obs: a função len retorna a qtd de caracteres da str
o fatiamento é usado para imprimir apenas uma fatia da string

o primeiro valor é o inicio, segundo é o final e depois de quantos em quantos ele vai
pular, por padrão pula de 1 em 1

a len mostra o tamanho da string, assim como em C
"""

variavel = "Olá mundo"
print(len(variavel))
print(variavel[2:8])
print(variavel[9:0:-2])
print(variavel[0:9:2])
print(variavel[::1])
print(variavel[::-1])