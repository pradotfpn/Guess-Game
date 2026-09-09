import random
import time
pontuacao = 0
pontuacaofinal = 0
sequencia = 0
def guessgame(pontuacaofinal, sequencia, tries, dificuldade):
    secret_number = random.randint(1, 100)
    while tries != 0:
        chute = int(input("\nDigite o valor do número que deseja adivinhar: "))
        if chute == secret_number:
            print("\n✅ Parabéns! você adivinhou o número secreto!!! 🥳")
            pontuacao = tries + (dificuldade * 2)
            print(f"🌟 Sua pontuação: {pontuacao}")
            pontuacaofinal += pontuacao
            sequencia += 1
            return pontuacaofinal, sequencia
        elif chute > secret_number:
            print(f"\n{chute} é maior do que ❓❓❓")
        else:
            print(f"\n{chute} é menor do que ❓❓❓")
        tries -= 1
        print(f"\nNúmero de tentativas restantes: {tries}\n")
    if tries == 0:
        pontuacao = 0
        print(f"❌ Você perdeu... O número secreto era: {secret_number}. Mais sorte na proxima! 🙂\n")
        sequencia = 0
        return pontuacaofinal, sequencia
while True:
    print("Bem vindo ao jogo de advinhação de números\n")
    time.sleep(1)
    print(f"🔥 Sequência de Vitorias: {sequencia} ")
    print(f"⭐ Pontuação Máxima: {pontuacaofinal}")
    time.sleep(1)
    dificuldade = int(input("\nSelecione a dificuldade:\n'1' para Fácil 🙂\n'2' para Médio 😐\n'3' para Díficil 😡\n'4' para IMPOSSIVEL 😈\nQualquer outra tecla para sair... \n\n"))
    match dificuldade:
        case 1:
            pontuacaofinal, sequencia = guessgame(pontuacaofinal, sequencia, 10, dificuldade)
        case 2:
             pontuacaofinal, sequencia = guessgame(pontuacaofinal, sequencia, 5, dificuldade)
        case 3:
             pontuacaofinal, sequencia = guessgame(pontuacaofinal, sequencia, 3, dificuldade)
        case 4:
             pontuacaofinal, sequencia = guessgame(pontuacaofinal, sequencia, 1, dificuldade)
        case _:
            print("Fim do programa...")
            break
    tryagain = int(input("Você deseja jogar novamente?\n'1' Para Sim\nQualquer outro para sair...\n"))
    match tryagain:
        case 1:
            continue
        case _:
            print("Obrigado por jogar!")
            print(f"Resultado final:")
            print(f"🌟 Pontos máximos: {pontuacaofinal}")
            print(f"🔥 Sequência final: {sequencia}")
            break