"""
introdução ao try/except
try = tentar executar o código
except = ocorreu algum erro ao tentar executar
try/catch em outras linguagens
exceções = erros

o try/except é usado para testar algum código com erro. (mesma estrutura do if/else).
por exemplo, se tiver um erro no meio do try, ele irá reconhecer o erro mas não irá
revelar o erro (relevar exceção), ele irá pular o erro e ir direto para o except.
"""

numero = input("Digite um número: (irei dobrá-lo)")

try:
    print("Str: ",numero)
    numero_1 = float(numero)
    print("float: ", numero_1)
    print(numero_1 * 2)
except:
    print("Isso não é um número.")

"""
if numero.isdigit():
    numero_1 = float(numero)
    print(numero_1 * 2)
else:
    print("Isso não é um número.")
"""
