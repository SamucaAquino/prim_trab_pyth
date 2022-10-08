
area_ser_pintada = float(input(f"Área a ser pintada m²: "))

cobertura_tinta_por_litro = float(1)
area_pint_litro = float(3)
litro_lata = float(18)
preç_lata = float(80)

demanda_tinta = int(area_ser_pintada / area_pint_litro) 
print(f"Demanda de tinta: {demanda_tinta}L")

if demanda_tinta <= litro_lata:
        print(f"Orçamento: R${preç_lata*1:}")
else:
        print(f"Orçamento: R${round(demanda_tinta/litro_lata)*preç_lata: .2f}")
if demanda_tinta <= litro_lata:
    print(f"1 lata -> 18L.")
else:
    print(f"{round(demanda_tinta/litro_lata)}Latas")

