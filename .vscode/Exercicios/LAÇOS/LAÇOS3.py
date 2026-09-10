# Exercicio 3 de Laços de repetição

nome = input("Digite seu nome: ").strip()
while len(nome) <= 3:
    nome = input("Nome muito pequeno!\nDigite seu nome novamente: ")
print("=" * 25)
idade = int(input("Digite sua idade: "))
while idade <= 0 or idade > 150:
    idade = float(input("Digite uma idade valida!\nDigite sua idade novamente: "))
print("=" * 25)
salario = float(input('Digite seu salario: '))
while salario <= 0:
    salario = float(input('Salário invalido!\nDigite novamente: '))
print("=" * 25)
sexo = input('Sexualidade: \n   f para feminino\n   m para masculino\n   o para outros\n Digite sua sexualidade: ')
while sexo not in ('f', 'm', 'o'):
    sexo = input('Digite um caracter valido!\nDigite sua sexualidade:')
print("=" * 25)
estadocivil = input('"s" para solteiro\n"c" para casado\n "v" para viúvo\n "d" para divorciado\nInsira seu estado civil: ')
while estadocivil not in ('s', 'c', 'v', 'd'):
    estadocivil = input('Insira um caracter valido!\nInsira seu estado civil:')
print("\n" + "=" * 25)
print(' DADOS CADASTRADOS')
print('=' * 25)
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f'Salário: R$ {salario:.2f}')
print(f"Sexo: {sexo.upper()}")
print(f'Estado Civil: {estadocivil.upper()}')
print("=" * 25)