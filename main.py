# Author: Salah Eddin Mohamed
# Date: 22/2/2022
# Institution: FCAI CU
# Email: salaheddin.mohamed12345@gmail.com
# Desc: This is a two-player mathematical
# game of strategy. It is played by two people with a pile of coins (or other
# tokens) between them. The players take turns removing coins from the pile,
# always removing a non-zero square number of coins (1, 4, 9, 16, …). The
# player who removes the last coin wins.
from random import randint


def check_if_possible(x, n):
    """
    Checks if move x is possible
    :param x: player input
    :param n: current number of coins
    :return: bool
    """
    i = 1
    # checks if player input is a square and is less than total number of coins
    while i * i != x:
        i += 1
        if i * i > x or i * i > n:
            return False
    return True


# This makes sure that the starting number of coins is random
coins = randint(10, 1000)

# This way, player changing is easier
# this boolean is inversed after each move
# and its value is used to get the player number
cur_player = False
player_name = {False: "Player 1", True: "Player 2"}

while coins > 0:
    print("Current number of coins:", coins)
    player_input = int(input(f"{player_name[cur_player]}'s Turn: "))
    if check_if_possible(player_input, coins):
        coins -= player_input
        if coins != 0:
            # inverse player after each move
            cur_player = not cur_player
    else:
        print("Invalid Move")
print(player_name[cur_player], "Wins!")
