# Faça um programa que leia 5 números e informe o maior número. // menor número também
print("=" * 25)
print("Programa de informar o maior número")
print("=" * 25)
num = 0
maior = float("-inf")
menor = float("inf")
for i in range(5):
    num = float(input(f"Insira {i + 1}º número: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print("=" * 25)
print(f"\nO maior número é: {maior}\n")
print("=" * 25)
print(f"\nO menor número é: {menor}\n")
print("=" * 25)