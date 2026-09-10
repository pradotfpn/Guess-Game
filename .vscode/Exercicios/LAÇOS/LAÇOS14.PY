# Programa que pede 10 números inteiros, calculo e mostrar numeros pares e impares
impar = 0
par = 0
soma = 0
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    soma += num
print("*" * 25)
print("\n RESULTADO FINAL\n")
print(f"Soma total: {soma}")
print(f"Quantidade de pares: {par}")
print(f"Quantidade de impares: {impar}\n")
print("*" * 25)