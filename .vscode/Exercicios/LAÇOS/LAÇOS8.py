# Faça um programa que leia 5 números e informe o maior, a soma e a média dos números.
soma = 0
maior = float("-inf")

print("=" * 25)
print("\nPrograma que lê números e exibe o maior, soma e média.\n")
print("=" * 25)

for i in range(5):
    num = float(input(f"Digite o {i + 1}º número: "))
    soma += num
    if num > maior:
        maior = num
media = soma / 5
print("=" * 25)
print(f"O maior número é: {maior:.2f}")
print(f"A soma destes números é: {soma:.2f}.")
print(f"A média destes números é: {media:.2f}.\n")
print("=" * 25)