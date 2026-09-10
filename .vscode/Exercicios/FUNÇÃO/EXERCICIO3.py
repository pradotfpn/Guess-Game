# encontrar palavras em frases
def contar_frase(frase, caracter):
    count = 0
    for i in frase: 
        if caracter.lower() == i.lower():
            count += 1
    print(f"A letra escolhida na frase tem {count} vezes")

frase = input("Digite uma frase e veja quantos caracteres tem naquela frase: ")

caracter = input("Digite uma letra: ")
while len(caracter) != 1:
    caracter = input("Digite APENAS uma letra: ")
contar_frase(frase, caracter)


