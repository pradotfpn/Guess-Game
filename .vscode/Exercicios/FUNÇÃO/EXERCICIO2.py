# Calculadora geral
def calculadora(x, y):
    print(f"A soma destes números é: {x + y}")
    print(f"A subtração destes números é: {x - y}")
    print(f"A multiplicação destes números é {x * y}")
    print(f"A divisão destes números é {x / y}")
num1 = float(input("Digite o primeiro número da calculadora: "))
num2 = float(input("Digite o segundo número da calculadora: "))
calculadora(num1, num2)