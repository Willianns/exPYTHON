while True:
  
    nota = float(input("Digite uma nota entre zero e dez: "))
    
    if 0 <= nota <= 10:
        break  
    else:
        print("Nota inválida. A nota deve estar entre zero e dez.")
        
print("Você inseriu a nota:", nota)



