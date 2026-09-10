# Programa que pede notas
print('Programa de listagem de notas.')
nota = float(input("Digite sua nota de 0 a 10: "))
while nota < 0 or nota > 10:
    print('Insira um valor valido!')
    nota = float(input("Digite sua nota: "))
print(f"Sua nota é {nota}.")
