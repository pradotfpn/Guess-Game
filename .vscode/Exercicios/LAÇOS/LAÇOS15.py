# Sequencia de Fibonacci
a = 0
b = 1
c = 0
num = int(input("Digite qual número você deseja na sequência de Fibonacci: "))
for i in range(num - 1):
    c = a + b
    a = b 
    b = c 
print("\n" + "*" * 25)
print(f"\nO número {num}º na sequência de Fibonacci é: {c}\n")
print("*" * 25)