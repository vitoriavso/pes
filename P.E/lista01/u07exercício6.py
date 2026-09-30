'''6 - Jogo do Pedra, Papel, Tesoura. Solicite as escolhas do jogador 1 e do jogador 2
(“pedra”, “papel” ou “tesoura”). Use condicionais para determinar quem ganhou:
• Pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra.
• Exiba uma mensagem como “Jogador 1 venceu!” ou “Empate!”.'''

jogador1 = input('Jogador 1, qual jogada você deseja fazer? ')
jogador2 = input('Jogador 2, qual jogada você deseja fazer? ')
if jogador1 == jogador2:
    print ('Empate!')
elif jogador1 == 'pedra' and jogador2 == 'tesoura':
    print ('O jogador 1 venceu!')
elif jogador2 == 'pedra' and jogador1 == 'tesoura':
    print ('O jogador 2 venceu!')
elif jogador1 == 'tesoura' and jogador2 == 'papel':
    print ('O jogador 1 venceu!')
elif jogador2 == 'tesoura' and jogador1 == 'papel':
    print ('O jogador 2 venceu!')
elif jogador1 == 'papel' and jogador2 == 'pedra':
    print ('Jogador 1 venceu!')
elif jogador2 == 'papel' and jogador1 == 'pedra':
    print ('Jogador 2 venceu!') 