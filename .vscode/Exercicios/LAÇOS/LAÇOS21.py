# Verificador de número primo
cont = 0
a = 1
b = 1
num = 0
while num <= 1:
    num = int(input("Digite um número inteiro para verificar se ele é primo ou não: "))
    if num <= 1:
        print('\nDigite um número inteiro valido para verificação de números primos!!\n') 
for i in range(1, num + 1):
    if num % i == 0:
        cont +=1
if cont > 2:
    print("Este número não é primo!")
else:
    print("Este número é primo!") 
