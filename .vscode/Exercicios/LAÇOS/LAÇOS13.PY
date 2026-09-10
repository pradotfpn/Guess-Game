# programa de exponenciação sem a funçao de potencia
contador = 1
num = 1
base = int(input("Digite o número de base: "))
expoente = int(input('Digite o número do expoente: '))
if expoente != 0:
    while contador <= expoente:
        num *= base
        contador += 1
    print(f'O resultado dessa potência é: {num}')
    if expoente < 0:
        contador = expoente
        while contador != 0:    
            num *= base
            contador += 1
        num = (+num)
        print(f'O resultado dessa potência é: {1 / num} ou 1/{num}')
else:
    print(f'O resultado dessa potência é: 1')
