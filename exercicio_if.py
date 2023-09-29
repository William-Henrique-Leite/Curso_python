num1= input("Digite o primeiro número: ") 
num2= input("Digite o segundo número: ") 

if num1 > num2:
    print(f"O primeiro valor={num1} é maior que o segundo valor={num2}")
elif num2 > num1:
    print(f"O segundo valor={num2} é maior que o primeiro valor={num1}")
else:
    print("Os valores são iguais")