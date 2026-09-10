# Calculo de crescimento de população utilizando laço de repetição

pais_a = 80000.0
pais_b = 200000.0
anos = 0
while pais_b > pais_a:
    pais_a *= 1.03
    pais_b *= 1.015
    anos += 1
print('=' * 25 )
print("CALCULO FINAL")
print('=' * 25 )
print(f"O Pais A demorou {anos} anos para ultrapassar o Pais B!")
print(f'População final do Pais A: {int(pais_a):,} habitantes'.replace(",", "."))
print(f'População final do Pais B: {int(pais_b):,} habitantes'.replace(",", "."))
print('=' * 25 )
