import random

def exibir_mensagens(mensagens):
    for mensagem in mensagens:
        print(mensagem)
        input("")

def introducao():
    mensagens = [
    "Olá!",
    "Bem-vindo ao mundo dos Pokémon!",
    "Meu nome é Carvalho!",
    "As pessoas chamam-me de o Professor Pokémon",
    "Este mundo é habitado por criaturas chamadas Pokémon!",
    "Para alguns, os Pokémon são animais de estimação, outros os usam para lutar. Como você mesmo!",
    "Eles vêm em todas as formas e tamanhos. Estamos descobrindo e pesquisando. Para mim, eu me considero um pesquisador Pokémon!"
    ]
    exibir_mensagens(mensagens)


def intro_inicial():
    mensagens = [
    f"Olá {nome}, agora você irá começar a sua jornada.",
    "Mas antes disso você terá de escolher um pokemon para ser seu companheiro!",
    "Primeiro nós temos o Bulbasaur!",
    "Por algum tempo após seu nascimento, ele utiliza os nutrientes que estão contidos na semente em seu dorso para crescer.",
    "Em seguida nós temos o Charmander!",
    "A chama em sua cauda mostra a força de sua força vital. Se Charmander estiver fraco, a chama também queimará fracamente.",
    "Por ultimo  nós temos o Squirtle!",
    "Após o nascimento, suas costas incha e endurece formando uma concha. Ele espalha uma espuma potente pela boca."

    ]
    exibir_mensagens(mensagens)
    
def pokemon_inicial():
    print("Agora depois de conhecer os três pokemon iniciais, qual você ira escolher\n")
    print("1 - Bulbasaur")
    print("2 - Charmander")
    print("3 - Squirtle")
    
def escolha_inicial():
    opcao_inicial = int(input("Escolha seu inicial: "))
    if opcao_inicial == 1:
        print("Vejo que decidiu escolher o Bulbasaur!")
        print("Ele é uma ótima escolha para aqueles que preferem uma abordagem mais equilibrada em sua jornada.") 
    elif opcao_inicial == 2:
        print("Vejo que decidiu escolher o Charmander!")
        print("Ele é uma ótima escolha para aqueles que preferem uma abordagem mais ofensiva em sua jornada. ")
    elif opcao_inicial == 3:
        print("Vejo que decidiu escolher o Squirtle!")
        print("Ele é uma ótima escolha para aqueles que preferem uma abordagem mais defensiva em sua jornada")
    else:
        print("Opção inválida, escolha novamente...")

def exibir_pokedex(pokedex):
    if len(pokedex) == 0:
        print("Sua Pokédex está vazia!")
    else:
        print("Pokémons capturados:")
        for pokemon in pokedex:
            print(pokemon)

def menu_jornada():
    print("\nEscolha a operação:")
    print("1 - Floresta de Viridian")
    print("2 - Monte Lua")
    print("3 - Pokédex")
    print("4 - Sair")

def explorar_mundo(nome, pokedex, pokebolas):
    opcao = int(input("Escolha o que deseja fazer: "))

    if opcao == 1:
        opcao = "Floresta de Viridian"
        pokebolas += pokebolas_ganhas()
        capturar_pokemon(opcao, pokedex,pokebolas)
    elif opcao == 2:
        opcao = "Monte Lua"
        pokebolas += pokebolas_ganhas() 
        capturar_pokemon(opcao, pokedex,pokebolas)
    elif opcao == 3:
        exibir_pokedex(pokedex)
    elif opcao == 4:
        print("Saindo do jogo.")
        exit()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        
def pokebolas_ganhas():
    return random.randint(0, 2)
        
def capturar_pokemon(mundo, pokedex, pokebolas):
    if mundo == "Floresta de Viridian":
        pokemon = random.choice(["Pidgey", "Rattata", "Caterpie", "Weedle"])
    else:
        pokemon = random.choice(["Geodude", "Zubat", "Onix", "Diglett"])
    print(f"Você entrou na {mundo} e encontrou um {pokemon}!")
    capturar = input("Você quer capturá-lo? (s/n): ")
    
    if capturar.lower() == "s":
        if pokemon in pokedex:
            print(f"O {pokemon} já está cadastrado na sua Pokédex.")
        else:
            if mundo == "Floresta de Viridian":
                chance_captura = 0.5
            else:
                chance_captura = 0.35
            
        if random.random() <= chance_captura:
            print(f"Parabéns! O {pokemon} foi capturado.")
            pokedex.append(pokemon)
        else:
                print(f"O {pokemon} escapou!")
                if pokebolas > 0:
                    nova_tentativa = input("Você quer tentar de novo? (s/n): ")
                    if nova_tentativa.lower() == "s":
                        pokebolas -= 1
                        capturar_pokemon(mundo, pokedex, pokebolas)
                    else:
                        print("Boa sorte em sua próxima tentativa.")
                else:
                    print("Você utilizou todas as suas tentativas.")
    else:
        print("O pokemon fugiu...")

def iniciar_jogo():
    introducao()
    #você está informando ao Python que a variável é global, ou seja, ela existe no escopo global do programa e pode ser acessada e modificada de qualquer lugar dentro do programa.
    global nome
    nome = input("Agora, diga-me, qual o seu nome?  ")
    intro_inicial()
    
    pokedex = []
    pokebolas = 3
    
    pokemon_inicial()
    escolha_inicial()
    while True: 
    
        menu_jornada()
        explorar_mundo(nome, pokedex, pokebolas)

#verifica se o script está sendo executado como o programa principal.        
if __name__ == "__main__":
    iniciar_jogo()
