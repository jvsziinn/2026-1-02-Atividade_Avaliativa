repeticoes = int(input("Quantos números serão digitados? "))
numeros = []
soma = 0
for i in range(repeticoes):
    valor = int(input("Digite um número: "))
    
    numeros.append(valor)
    soma += valor
media = soma / repeticoes
maior = max(numeros)
menor = min(numeros)
acima_media = 0
for numero in numeros:
    if numero > media:
        acima_media += 1
print("Soma total:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Quantidade acima da média:", acima_media)