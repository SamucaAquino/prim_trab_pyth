sal_hora = float(input(f"Informe quanto você recebe p/ hora: R$"))
horas_trab_mes = float(input(f"Informe quantas horas trabalhas no mês: "))

sal_base = float(sal_hora * horas_trab_mes)
print(f"(+)Salário Bruto: R${sal_base:.2f}")

sal_bruto = sal_base
ir = float(sal_bruto * 11/100)
inss = float(sal_bruto * 8/100)
sindi = float(sal_bruto * 5/100)
sal_liqui = float(sal_base - ir - inss - sindi)
total_desc = float(ir + inss + sindi)

print(f"   (-)IR: R${ir:.2f}")
print(f"   (-)INSS: R${inss:.2f}")
print(f"   (-)Sindicato: R${sindi:.2f}")
print(f"(=)Desconto total: R${total_desc:.2f}")
print(f"(=)Salário Líquido: R${sal_liqui:.2f}")