"""
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
usado exatamente igual a linguagem C, usando a % e no final usar entre parentese
respectivamente
"""

nome = "William"
preco = 99.89
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %04X" % (15, 15))