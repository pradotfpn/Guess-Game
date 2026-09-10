# Ordenação de conjuntos
def bubblesort(vet_num):
    largura = len(vet_num)
    for i in range(largura):
        for j in range(0, largura - 1 - i):
            if vet_num[j] > vet_num[j + 1]:
                vet_num[j + 1] , vet_num[j] = vet_num[j] , vet_num[j + 1]
    print(f"O conjunto dos números ordenados são: \n{vet_num}")

def  selectionsort(vet_num):
    largura = len(vet_num)
    for i in range(largura):
        maior = float('-inf')
        for j in range(0, largura - i):
            if vet_num[j] > maior:
                maior = vet_num[j] # salva o número do indice na variavel maior
                indice = j # salva a posição do número na variavel indice
        aux = vet_num[largura - i - 1] # salva o ultimo número da lista
        vet_num[largura - i - 1] = maior # sobrescreve o ultimo número da lista com o número maior
        vet_num[indice] = aux # sobrescreve o número que foi trocado do indice maior
    print(f"\nO conjunto dos números ordenados são: \n{vet_num}\n")


vet_num = []
num = int(input("Digite quantos números quer ordenar: "))
for i in range(num):
    vet_num.append(float(input("\nDigite o valor que queira ordenar: ")))
while True:
    ordenacao = str(input("Qual ordenação você deseja escolher?\n'1'para bubble sort \n'2' para selection sort\n ou qualquer outro para sair: "))
    match ordenacao:
        case '1':
            bubblesort(vet_num)
        case '2':
            selectionsort(vet_num)
        case _:
            print("Fim do programa...")
            break
 
    






    