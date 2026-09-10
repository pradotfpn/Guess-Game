# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
soma = 0
print("*" * 25)
print("\nPrograma de gerar números inteiros entre intervalos recebidos pelo usúario\n")
print("*" * 25)
num1 = int(input("\nDigite o primeiro número menor: "))
num2 = int(input("Digite o segundo número maior: "))
inicio = min(num1 , num2)
fim = max(num1, num2)
for i in range(inicio + 1, fim):
    soma += i
    print(i, end=" ")
print(f"\nA soma destes números é: {soma}")