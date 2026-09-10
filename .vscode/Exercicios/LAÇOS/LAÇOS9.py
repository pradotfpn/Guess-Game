# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50
num = 1
print("Apenas números impares: ")
while num <= 50:
    if num % 2 == 1:
        print(num, end=" ")
    num += 1
for i in range(1, 51, 2):
    print(i, end=" ")