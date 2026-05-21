a = int(input("Digite a quantidade de números:"))
import random
for numero in range (a):
    a = random.randint(1,100)
    print(f'{numero+1}° {a}')