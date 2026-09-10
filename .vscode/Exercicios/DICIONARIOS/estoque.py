# FAÇA UM PROGRAMA PARA CRIAR ESTOQUE DE PRODUTOS COM REGISTROS

vet_estoque = []

def produtos():
    print("\nEstoque de produtos: ")
    for i in range(0, 2):
        registro_estoque = {}
        registro_estoque['Código do Produto: '] = i + 1
        registro_estoque['Nome do Produto: '] = str(input("\nDigite o nome do produto: "))
        registro_estoque['Preço do Produto: '] = float(input("Digite o valor do produto: "))
        registro_estoque['Quantidade do produto: '] = int(input("Digite a quantidade do produto: "))
        vet_estoque.append(registro_estoque)
def mostrar_produtos(x):
    x -= 1
    print("\nTabela de Preços:\n")
    print(f"Código do produto: {vet_estoque[x]['Código do Produto: ']:02d}")
    print(f"Nome do produto: {vet_estoque[x]['Nome do Produto: ']}")
    print(f"Preço do produto: R${vet_estoque[x]['Preço do Produto: ']:.2f}")
    print(f"Quantidade do produto: {vet_estoque[x]['Quantidade do produto: ']}\n")
produtos()
print(f"\nQuantidade de produtos diferentes armazenados no estoque: {len(vet_estoque)}")
num = int(input("Digite o Código do produto que queira visualizar: "))
while num <= 0 or num > len(vet_estoque):
    print("\nEste número de código não está cadastrado!")
    num = int(input(f"Insira um valor entre 1 e {len(vet_estoque)}: "))
mostrar_produtos(num)



