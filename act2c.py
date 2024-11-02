numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

copo = numero1

if numero2 < copo:
    copo = numero2
if numero3 < copo:
    copo = numero3
print(f'O menor número digitado foi {copo}')