h_altura = float(input("Qual a sua altura: "))
sexo = str(input("Dama ou Macho: "))

macho = float((72.7 * h_altura) - 58)
dama = float((61.1 * h_altura)- 44.7)

if(sexo == "macho"):
    print(f"Seu peso ideal é: {macho:.2f}")
    
elif(sexo == "dama"):
    print(f"Seu peso ideal é: {dama:.2f}")

else:
    print(f"Err#")

