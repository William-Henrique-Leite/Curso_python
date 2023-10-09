num1 = input("Digite um número: ")
if num1.isdigit():
    num1_int = int(num1)
    calculo = num1_int % 2
    if calculo == 0:
        print("O número é par.")
    else:
        print("O número é impar.")
else:
    print("Digite um valor válido.")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

hora = input("Digite a hora: ")
if int(hora) >= 0 and int(hora) <= 11:
    print("Bom dia usuário.")
elif int(hora) >= 12 and int(hora) <= 17:
    print("Boa tarde usuário.")
elif int(hora) >= 18 and int(hora) <= 23:
    print("Boa noite usuário.")
else:
    print("Digite um valor válido.")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

nome = input("Digite seu nome: ")
if len(nome) <= 4:
    print("Seu nome é curto.")
elif len(nome) >=5 and len(nome) <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
