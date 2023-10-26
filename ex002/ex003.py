num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero"))

maior = num1
menor = num1

if num2 > num1:
    maior = num2

if num2 < menor:
    menor = num2

if num3 > maior:
    maior = num3

if num3 < menor:
    menor = num3

print ("O maior numero é:", maior)
print ("O menor numero é:", menor)