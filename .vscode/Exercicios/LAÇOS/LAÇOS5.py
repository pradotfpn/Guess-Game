# Calculo de crescimento de população utilizando laço de repetição PARTE 2
print('=' * 25 )
print('\nCalculo de crescimento de população\n')
print('=' * 25 )
pais_a = int(input('Digite a população do Pais A: '))
pais_b = int(input('Digite a população do Pais B: '))
multiplicador_a = float(input('Digite a taxa de crescimento anual do Pais A em decimais: '))
multiplicador_b = float(input('Digite a taxa de crescimento anual do Pais B em decimais: '))
anos = 0
while pais_b > pais_a:
    pais_a += pais_a * multiplicador_a 
    pais_b += pais_b * multiplicador_b
    anos += 1
print('=' * 25 )
print("CALCULO FINAL")
print('=' * 25 )
print(f"O Pais A demorou {anos} anos para ultrapassar o Pais B!")
print(f'População final do Pais A: {int(pais_a):,} habitantes'.replace(",", "."))
print(f'População final do Pais B: {int(pais_b):,} habitantes'.replace(",", "."))
print('=' * 25 )
