from board import board
import random

class player:
    def __init__(self):
        self.cash = 1500
        self.pos = 0
        self.get_out_of_jail_free = 0
        self.last_payment = None

    def move(self):
        if (self.pos + (dice_sum := random.randint(1, 6) + random.randint(1, 6)) - 40) >= 0:
            self.pos += dice_sum - 40
            self.cash += 400
        else:
            self.pos += dice_sum
        board[self.pos].landing(self)

    def buy_possibility(self):
        pass


class strategy(player):
    pass

test = strategy()
for i in range(1000000):
    test.move()
print(test.cash/1000000)
