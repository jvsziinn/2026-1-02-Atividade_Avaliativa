a = int(input("Digite um número: "))
soma = 0
for divisor in range(1,a):
    if a%divisor ==0:
        soma += divisor
if soma == a:
        print(f'{a} É perfeito')
else:
        print(f'{a} É imperfeito')