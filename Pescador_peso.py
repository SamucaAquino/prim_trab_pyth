peso = float(input("Informe o peso: "))

if peso > 50:
    print("Peso excedido! Peso limite: 50kg.")
    excedido = float(peso - 50) 
    multa = float(4*excedido)
    print(f"Peso excedido: {excedido: .2f}kg")
    print(f"Multa: ${multa:.2f}")
else:	
    print(f"Dentro do limite.")

