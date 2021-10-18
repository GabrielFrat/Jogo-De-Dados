from random import randrange
import sys


print('=========================================================')
print('                    Jogo de Dados                        ')
print('            Humano        X        Mr. Popo              ')
print('=========================================================')
confirma = input('Você gostaria de jogar contra o Mr. Popo? (S/N): ')


winPlayer = 0
winPopo = 0
cont = 0

if confirma == 'S':
    while confirma == 'S':
        cont += 1
        popo = randrange(1, 6)
        player = randrange(1, 6)
        if popo > player:
            print(f'Mr. Popo: {popo} x Player: {player}!')
            print('O Mr. Popo ganhou!')
            winPopo += 1
        elif player > popo:
            print(f'Mr. Popo: {popo} x Player: {player}!')
            print('É isso ai!!! Você ganhou!')
            winPlayer += 1
        elif player == popo:
            print(f'Mr. Popo: {popo} x Player: {player}!')
            print('Uauuuu!!! Nós temos um empate!')
        else:
            print('Estamos com problemas técnicos.')

        confirma = input('Você gostaria de jogar novamente? (S/N): ')
elif confirma == 'N':
    print('Que pena! Quem sabe na próxima vez')
else:
    print('Opção Inválida!')

if cont > 0:
    print('=======================================================')
    print(f'Quantidade de vezes que você venceu: {winPlayer}      ')
    print(f'Quantidade de vitórias do Mr. Popo: {winPopo}         ')
print('=======================================================')
print('                 Término do Jogo                       ')
print('=======================================================')

