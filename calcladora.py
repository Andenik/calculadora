#corpo calculadora


operadores = '+-/*'

while True:
    #recolhe um numero
    numero_1 = input("Digite um numero: ")
    #checa se o numero digitado e um numero
    if numero_1.isdigit() == False:
        print("Voce nao digitou um numero tente novamente")
        continue

    numero_2 = input("Digite outro numero: ")
    if numero_2.isdigit() == False:
        print("Voce nao digitou um numero tente novamente")
        continue

    operador = input("Digite um Operador +-/*: ")
    if operador not in operadores:
        print('voce nao digitou um operador')
    
    if len(operador) > 1:
        print('Digite apenas um operador')
