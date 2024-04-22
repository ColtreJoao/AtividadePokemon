import random

# Lista de mensagens a serem exibidas
mensagens = [
    "Olá!",
    "Bem-vindo ao mundo dos Pokémon!",
    "Meu nome é Carvalho!",
    "As pessoas chamam-me de o Professor Pokémon",
    "Este mundo é habitado por criaturas chamadas Pokémon!",
    "Para alguns, os Pokémon são animais de estimação, outros os usam para lutar. Como você mesmo!",
    "Eles vêm em todas as formas e tamanhos. Estamos descobrindo e pesquisando. Para mim, eu me considero um pesquisador Pokémon!"
]

# Loop para exibir cada mensagem
for mensagem in mensagens:
    print(mensagem)
    input("")

nome = input("Agora, diga-me, qual o seu nome?  ")
nome_jogador = nome

# Lista de mensagens a serem exibidas
mensagens = [
    f"Olá {nome_jogador}, agora você irá começar a sua jornada.",
    "Você agora terá duas opções para se aventurar!",
    "Você poderá escolher em ir para a Floresta de Viridian ou para o Monte Lua!",
    "Mas lembre-se, dependendo de onde for existirão diferentes tipos de Pokémon!"
]

# Loop para exibir cada mensagem
for mensagem in mensagens:
    print(mensagem)
    input("")

# Inicialização da Pokedex
pokedex = []

while True:
    tentativas_extras = 3
    print("\nEscolha a operação:")
    print("1 - Floresta de Viridian")
    print("2 - Monte Lua")
    print("3 - Pokédex")
    print("4 - Sair")

    opcao = int(input("Escolha o que deseja fazer: "))

    if opcao == 1:
        opcao = "Floresta de Viridian"
        pokemon_floresta = random.choice(["Pidgey", "Rattata", "Caterpie", "Weedle"])
        print(f"Você entrou na {opcao} e encontrou um {pokemon_floresta}!")
        opcao_captura = input("Você quer capturá-lo? (s/n)")
        if opcao_captura == "s":
            if pokemon_floresta in pokedex:
                print(f"O {pokemon_floresta} já está cadastrado na sua Pokédex.")
            else:
                chance_captura = 0.5
                if random.random() < chance_captura:
                    print(f"Parabéns! O {pokemon_floresta} foi capturado.")
                    pokedex.append(pokemon_floresta)
                else:
                    print(f"O {pokemon_floresta} escapou!")
                    if tentativas_extras > 0:
                        nova_tentativa = input("Você quer tentar de novo? (s/n)")
                        if nova_tentativa == "s":
                            tentativas_extras -= 1
                            if random.random() < chance_captura:
                                print(f"Parabéns! O {pokemon_floresta} foi capturado.")
                                pokedex.append(pokemon_floresta)
                            else:
                                print(f"O {pokemon_floresta} escapou!")
                                tentativas_extras -= 1
                        else:
                            print("Boa sorte em sua próxima tentativa.")
                    else:
                        print("Você utilizou todas as suas tentativas.")
        else:
            print("Você decidiu não capturar este Pokémon.")

    elif opcao == 2:
        opcao = "Monte Lua"
        pokemon_caverna = random.choice(["Geodude", "Zubat", "Onix", "Diglett"])
        print(f"Você entrou na {opcao} e encontrou um {pokemon_caverna}!")
        opcao_captura = input("Você quer capturá-lo? (s/n)")
        if opcao_captura == "s":
            if pokemon_caverna in pokedex:
                print(f"O {pokemon_caverna} já está cadastrado na sua Pokédex.")
            else:
                chance_captura = 0.35
                if random.random() < chance_captura:
                    print(f"Parabéns! O {pokemon_caverna} foi capturado.")
                    pokedex.append(pokemon_caverna)
                else:
                    print(f"O {pokemon_caverna} escapou!")
                    if tentativas_extras > 0:
                        nova_tentativa = input("Você quer tentar de novo? (s/n)")
                        if nova_tentativa == "s":
                            tentativas_extras -= 1
                            if random.random() < chance_captura:
                                print(f"Parabéns! O {pokemon_caverna} foi capturado.")
                                pokedex.append(pokemon_caverna)
                            else:
                                print(f"O {pokemon_caverna} escapou!")
                                tentativas_extras -= 1
                        else:
                            print("Boa sorte em sua próxima tentativa.")
                    else:
                        print("Você utilizou todas as suas tentativas.")
        else:
            print("Você decidiu não capturar este Pokémon.")

    elif opcao == 3:
        opcao = "Pokedex"
        if len(pokedex) == 0:
            print("Sua Pokédex está vazia!")
        else:
            print("Pokémons capturados:")
            for pokemon in pokedex:
                print(pokemon)

    elif opcao == 4:
        print("Saindo do jogo.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
