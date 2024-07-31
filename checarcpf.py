"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = input('Digite seu cpf: ')

# x = [cpf.pop(-1), cpf.pop(-1)]

cpf = cpf.replace('.','',2)
cpf = cpf.replace('-','')

mult = 10

cpf_lista = []
for i in cpf:
    cpf_lista.append(i)

cpf_lista2 = cpf_lista.copy()              
x = [cpf_lista.pop(-1), cpf_lista.pop(-1)]
cpf_lista_sem_digito = []
for i in cpf_lista:
    i = int(i)
    i = i * mult
    cpf_lista_sem_digito.append(i)
    mult -= 1

soma = sum(cpf_lista_sem_digito)
soma = soma * 10
soma = soma % 11
digito = 0
if soma > 9:
    digito = 0
else:
    digito = soma

x2 = [cpf_lista2.pop(-1)]
digito2 = 0
mult2 = 11
cpf_lista_sem_digito2 = []
for i in cpf_lista2:
    i = int(i)
    i = i * mult2
    cpf_lista_sem_digito2.append(i)
    mult2 -= 1

soma2 = sum(cpf_lista_sem_digito2)
soma2 *= 10
soma2 %= 11

if soma > 9:
    diigito2 = 0
else:
    digito2 = soma2

print(digito)
print(digito2)



         
         
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
         
    
      
       
    



