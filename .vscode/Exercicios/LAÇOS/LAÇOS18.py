# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
menor = float("inf")
maior = float("-inf")
soma = 0
num = -1
while num < 0 or num > 1000:
    num = int(input('Digite quantos números você quer botar no conjunto entre 0 a 1000: '))
    if num < 0 or num > 1000:
        print("Digite um número entre 0 a 100")
for i in range(num):
    n = float(input(f"Digite o {i + 1}º termo: "))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n 
print("\n" + "*" * 25)
print(f"Quantidade números inseridos no conjunto: {num}")
print(f"A soma do conjunto é: {soma}")
print(f"O número menor do conjunto é: {menor}")
print(f"O número maior do conjunto é: {maior}")
print("\n" + "*" * 25)
