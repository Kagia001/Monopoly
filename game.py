from board import board
from player import player

player1 = player(None)
player2 = player(None)

for i in range(100):
    player1.move()
    player2.move()