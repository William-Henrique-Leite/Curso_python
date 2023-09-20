#se der errro ou of range significa que acabaram os valores
#use o format com uma determinada quantidade de valores, vou dar o print com chaves, na mesma quantidade de valores
#o nome3 é um parametro nomeado usado nas variaveis
#quando uma função esta dentro de um objeto se chama de metodo, por exemplo o format com ponto no final 

a = "A"
b = "B"
c = 1.1
string = "a={nome1} b={nome2} c={nome3:.2f}"
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)
