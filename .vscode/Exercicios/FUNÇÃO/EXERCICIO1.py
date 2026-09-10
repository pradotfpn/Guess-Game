# Calculadora com função
def valores():
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    return x, y 
def soma():
    x, y = valores()
    print(f"O resultado da soma é: {x + y}")
def subtracao():
    x, y = valores()
    print(f"O resultado da subtração é: {x - y}")
def multiplicacao():
    x, y = valores()
    print(f"O resultado da multiplicação é {x * y}")

def divisao():
    x, y = valores()
    while y == 0:
        print("O valor não pode ser zero na divisão! ")
        x, y = valores()
    print(f"O resultado da divisão é {x / y}")
while True:
    print("\n     CALCULADORA      \n")
    print("Digite 1 para adição\nDigite 2 para subtração\nDigite 3 para multiplicação")
    print("Digite 4 para divisão\n")
    num = (input("Digite outro número para sair: "))
    match num:
        case "1":
            soma()
        case "2":
            subtracao()
        case "3":
            multiplicacao()
        case "4":
            divisao()
        case _:
            break 
        
