diasTotais = int(input("Digite a idade em dias: "))

anos = diasTotais // 365
dias_restantes = diasTotais % 365

meses = dias_restantes // 30

dias = dias_restantes % 30

print(f"{anos} anos, {meses} meses e {dias} dias")

