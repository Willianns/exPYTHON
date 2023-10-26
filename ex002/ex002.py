nota1 = float(input("Digite a prímeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) /2
print ("Sua media foi:", media)

if media == 10:
    print ("Aprovado com DIstinção")
elif media >= 7:
    print ("Aprovado")
else:
   print ("Reprovado")