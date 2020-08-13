import random
from board import board

class player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.cash = 1500
        self.pos = 0
        self.get_out_of_jail_free = 0
        self.last_payment = None

    def move(self):
        if (self.pos + (dice_sum:=random.randint(1,6)+random.randint(1,6))-40) >= 0:
            self.pos += (dice_sum-40)
        else:
            self.pos += (dice_sum)
        board[self.pos].on_landing(self)

        