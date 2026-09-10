# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10

print("*" * 25)
print("\nTabuada.\n")
print("*" * 25)
num = int(input("\nDigite um número de 1 a 10 para ver a tabuada dele: "))
while num < 1 or num > 10:
    num = int(input("Digite um número entre 1 a 10!!: "))
print(f"\nTabuada de {num}:\n")
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")