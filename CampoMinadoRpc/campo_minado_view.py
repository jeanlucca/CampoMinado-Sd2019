from os import remove
import json

objeto = CampoMinado(3, 3)
objeto.imprima_tabuleiro()

print("Jogo /Campo Minado ")

def start ():
    if objeto.proxima_jogada():
        linha = int(input("Posição da linha :"))
        coluna = int(input("Posição da coluna :"))
        objeto.jogada(linha,coluna)
        start()
    else:
        print("Fim")


def partida():
    if isfile("game.json"):
        result = str(input("Quer continuar no jogo salvo?\n"))
        if result == "yes":
            arquivo = open("game.json")
            game = json.loads(arquivo.read())
            objeto.restaurar(game)
            arquivo.close()
        else:
            remove("game.json")

    start()

partida()