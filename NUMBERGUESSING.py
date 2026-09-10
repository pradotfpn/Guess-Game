import random
import time
pontuacao = 0
pontuacaofinal = 0
sequencia = 0
textos_do_jogo = {
    "pt": {
        "bem_vindo": "Bem vindo ao jogo de advinhação de números",
        "sequencia_vitorias": "Sequência de Vitorias: ",
        "pontuacao_maxima": "Pontuação Máxima: ",
        "dificuldade": "Selecione a dificuldade:\n'1' para Fácil\n'2' para Médio\n'3' para Díficil\n'4' para IMPOSSIVEL\nQualquer outro número inteiro para sair... \n\n",
        "dificuldade_valida": "Insira um valor inteiro válido!\n",
        "chute": "Digite o valor do número que deseja adivinhar: ",
        "tentativas_restantes": "Número de tentativas restantes: ",
        "acertou": "Parabéns! você adivinhou o número secreto!!!",
        "pontuacao": "Sua pontuação: ",
        "maior": "é maior do que o número secreto",
        "menor": "é menor do que número secreto",
        "perdeu": "Você perdeu... O número secreto era: ",
        "resultado_final": "Resultado final:",
        "pontos_maximos": "Pontos máximos: ",
        "sequencia_final": "Sequência final: ",
        "fim_programa": "Fim do programa...",
        "jogar_novamente": "Você deseja jogar novamente?\n'1' Para Sim\nQualquer outro número inteiro para sair...\n",
        "obrigado_jogar": "Obrigado por jogar!",
        },
    "en": {
        "bem_vindo": "Welcome to the number guessing game",
        "sequencia_vitorias": "Winning Streak: ",
        "pontuacao_maxima": "Maximum Score: ",
        "dificuldade": "Select the difficulty:\n'1' for Easy\n'2' for Medium\n'3' for Hard\n'4' for IMPOSSIBLE\nAny other integer to exit... \n\n",
        "dificuldade_valida": "Please enter a valid integer!\n",
        "chute": "Enter the number you want to guess: ",
        "tentativas_restantes": "Remaining attempts: ",
        "acertou": "Congratulations! You guessed the secret number!!!",
        "pontuacao": "Your score: ",
        "maior": "is greater than the secret number",
        "menor": "is less than the secret number",
        "perdeu": "You lost... The secret number was: ",
        "resultado_final": "Final result:",
        "pontos_maximos": "Maximum points: ",
        "sequencia_final": "Final sequence: ",
        "fim_programa": "End of program...",
        "jogar_novamente": "Do you want to play again?\n'1' For Yes\nAny other integer to exit...\n",
        "obrigado_jogar": "Thank you for playing!",
    },
}

linguagem = input("Escolha o idioma do jogo:\nDigite 'pt' para Português ou 'en' para Inglês: ").lower()
if linguagem not in textos_do_jogo:
    print("\nIdioma não suportado. O jogo será iniciado em português.")
    linguagem = "pt"
def guessgame(pontuacaofinal, sequencia, tries, dificuldade):
    secret_number = random.randint(1, 100)
    while tries != 0:
        try:
            chute = int(input(f"\n{textos_do_jogo[linguagem]['chute']}"))
        except ValueError:
            print(f"\n{textos_do_jogo[linguagem]['dificuldade_valida']}")
            continue
        if chute == secret_number:
            print(f"\n{textos_do_jogo[linguagem]['acertou']}")
            pontuacao = tries + (dificuldade * 5)
            print(f"{textos_do_jogo[linguagem]['pontuacao']}{pontuacao}")
            pontuacaofinal += pontuacao
            sequencia += 1
            return pontuacaofinal, sequencia
        elif chute > secret_number:
            print(f"\n{chute} {textos_do_jogo[linguagem]['maior']}")
        else:
            print(f"\n{chute} {textos_do_jogo[linguagem]['menor']}")
        tries -= 1
        print(f"\n{textos_do_jogo[linguagem]['tentativas_restantes']}{tries}\n")
    if tries == 0:
        pontuacao = 0
        print(f"{textos_do_jogo[linguagem]['perdeu']}{secret_number}. Mais sorte na proxima! \n")
        sequencia = 0
        return pontuacaofinal, sequencia
while True:
    print(f"\n{textos_do_jogo[linguagem]['bem_vindo']}")
    time.sleep(1)
    print(f"{textos_do_jogo[linguagem]['sequencia_vitorias']}{sequencia}")
    print(f"{textos_do_jogo[linguagem]['pontuacao_maxima']}{pontuacaofinal}")
    time.sleep(1)
    while True:
        try:
            dificuldade = int(input(f"\n{textos_do_jogo[linguagem]['dificuldade']}"))
            break
        except ValueError:
            print(f"\n{textos_do_jogo[linguagem]['dificuldade_valida']}")
            continue
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
            print(f"{textos_do_jogo[linguagem]['resultado_final']}")
            print(f"{textos_do_jogo[linguagem]['pontos_maximos']}{pontuacaofinal}")
            print(f"{textos_do_jogo[linguagem]['sequencia_final']}{sequencia}")
            print(f"{textos_do_jogo[linguagem]['fim_programa']}")
            break
    while True:
        try:
            tryagain = int(input(f"{textos_do_jogo[linguagem]['jogar_novamente']}"))
            break
        except ValueError:
            print(f"\n{textos_do_jogo[linguagem]['dificuldade_valida']}\n")
            continue
    match tryagain:
        case 1:
            continue
        case _:
            print(f"\n{textos_do_jogo[linguagem]['obrigado_jogar']}")
            print(f"{textos_do_jogo[linguagem]['resultado_final']}")
            print(f"{textos_do_jogo[linguagem]['pontos_maximos']}{pontuacaofinal}")
            print(f"{textos_do_jogo[linguagem]['sequencia_final']}{sequencia}")
            print(f"{textos_do_jogo[linguagem]['fim_programa']}")
            break