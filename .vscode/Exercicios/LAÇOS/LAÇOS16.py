# Sequência de Fibonacci até o número solicitado do usuário
a = 0
b = 1
c = 0
contador = 0
num = int(input("Digite o número máximo da Sequência de Fibonacci: "))
while c < num and a + b < num:
    c = a + b
    a = b
    b = c 
    contador += 1
    print(c, end=" ")
print(f"\nOs números na sequência foram: {contador}.")