# Programa que calcula fatorial e limita ao usuário a escrever entre 1 a 16
resultadofinal = 0 
while True:
    num = int(input("Digite o número inteiro (max:16) para calcular o fatorial: "))
    if num < 0 or num > 16:
        print("Digite um número inteiro! Entre 0 a 16.") 
    elif num == 0 or num == 1:
        print(f"\nO resultado final do {num}! é: 1\n")
        break
    else:
        break
while num > 1:
    numfixo = num 
    resultado = num
    while num != 1:
        num -= 1
        resultadofinal = resultado * num
        resultado = resultadofinal
    print("\n" + "*" * 25)
    print(f"\nO resultado final do {numfixo}! é: {resultadofinal}\n")
    print("*" * 25)
