from random import randint

print("""
======================================================================================
                        Regras do Jogo: O Robô e a Bateria
======================================================================================

    * O robô não pode sair dos limites da matriz (0 a 9 em ambas as direções).
    * O jogador informa uma sequência de comandos um de cada vez.
    * O jogador pode continuar informando comandos até digitar "parou".

    Os comandos disponíveis são:
        * "Cima" (W) > Move o robô uma posição para cima.
        * "Baixo" (S) > Move o robô uma posição para baixo.
        * "Esquerda" (A) > Move o robô uma posição para a esquerda.
        * "Direita" (D) > Move o robô uma posição para a direita.

======================================================================================""")


tabuleiro_jogoDoRobo = [
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""]
    ]
  
roboLinha = randint(0, 9)
roboColuna = randint(0, 9)
bateriaLinha = randint(0, 9)
bateriaColuna = randint(0, 9)
tabuleiro_jogoDoRobo[roboLinha][roboColuna] = 'RB'
tabuleiro_jogoDoRobo[bateriaLinha][bateriaColuna] = 'BT'

while bateriaLinha == roboLinha and bateriaColuna == roboColuna:
    bateriaLinha = randint(0, 9)
    bateriaColuna = randint(0, 9)

def imprimir_tabuleiro(lista):
    for linha in lista:
        print("|".join((str(item) + "    ")[:4]  if item else "____" for item in linha))


def sequência_comandos(lista,x_robo,y_robo,x_bateria,y_bateria): # a não ser que tire o while das perguntas e use so a entrada de usuario como parametro
   

    lista_sequencia_comandos=[]
    sequencia_comandos = input("informe a sequencia:").upper()

    while sequencia_comandos != "PAROU":
        
        lista_sequencia_comandos.append(sequencia_comandos)
        sequencia_comandos = input("informe a sequencia:").upper()
    
    for letra in lista_sequencia_comandos:
        lista[x_robo][y_robo] = '____'
        

        if letra == "W" and x_robo > 0 :
            x_robo -= 1 
             #uma linha atras        
        elif letra == "S" and x_robo < len(lista) -1:   
            x_robo += 1 
             # uma linha pra frente 
        elif letra == "A" and y_robo > 0 :
            y_robo -= 1
            # uma coluna atras
        elif letra == "D" and y_robo < len(lista)-1: 
            y_robo += 1
            # uma coluna pra frente
        else:
            print("Não é possível ir por este caminho")
            imprimir_tabuleiro(lista)
            pergunta = input("Deseja jogar novamente? (SIM/NÃO): ").upper()
            if pergunta == "SIM":
                return iniciar_novo_jogo()
            if pergunta == "NÃO" or pergunta == "NAO":
                print("Obrigado por jogar!")
                break
    
        lista[x_robo][y_robo] = 'RB'
    
    while True:
        if x_robo == x_bateria and y_robo == y_bateria:
            print("Você venceu!")
            imprimir_tabuleiro(lista)
            pergunta = input("Deseja jogar novamente? (SIM/NÃO): ").upper()
            if pergunta == "SIM":
                return iniciar_novo_jogo()
            if pergunta == "NÃO" or pergunta == "NAO":
                print("Obrigado por jogar!")
                break
        
        else:
            print("Não foi dessa vez")
            imprimir_tabuleiro(lista)
            pergunta = input("Deseja jogar novamente? (SIM/NÃO): ").upper()
            if pergunta == "SIM":
                return iniciar_novo_jogo()
            if pergunta == "NÃO" or pergunta == "NAO":
                print("Obrigado por jogar!")
                break


def iniciar_novo_jogo():
   
    tabuleiro_jogoDoRobo = [
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""]
    ]
  
    roboLinha = randint(0, 9)
    roboColuna = randint(0, 9)
    bateriaLinha = randint(0, 9)
    bateriaColuna = randint(0, 9)
    tabuleiro_jogoDoRobo[roboLinha][roboColuna] = 'RB'
    tabuleiro_jogoDoRobo[bateriaLinha][bateriaColuna] = 'BT'

    while bateriaLinha == roboLinha and bateriaColuna == roboColuna:
        bateriaLinha = randint(0, 9)
        bateriaColuna = randint(0, 9)

    imprimir_tabuleiro(tabuleiro_jogoDoRobo)
    sequência_comandos(tabuleiro_jogoDoRobo,roboLinha,roboColuna,bateriaLinha,bateriaColuna)


imprimir_tabuleiro(tabuleiro_jogoDoRobo)
chamado_sequência_comandos = sequência_comandos(tabuleiro_jogoDoRobo,roboLinha,roboColuna,bateriaLinha,bateriaColuna)
