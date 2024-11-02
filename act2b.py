a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a > b + c or b > a + c or c > a + b:
    print("Os valores", a, ", ", b, "e ", c, "não formam um triângulo.")
else:
    s = (a + b + c) / 2
    area = s * (s - a) * (s - b) * (s - c) ** 0.5
    print("A área do triângulo é:", area)