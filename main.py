# Author: Salah Eddin Mohamed
# Date: 22/2/2022
# Institution: FCAI CU
# Email: salaheddin.mohamed12345@gmail.com
from random import randint


def is_sqr(n):
    """
    Checks if a number is a square
    :param n: the number to be checked
    :return: boolean
    """
    i = 1
    while i * i < n:
        i += 1
    return True if i * i == n else False


def valid_move(x, n):
    """
    Checks if move x is possible
    :param x: player input
    :param n: current number of coins
    :return: boolean
    """
    return True if is_sqr(x) and x <= n else False


def main_loop():
    """
    The Game's Main Loop Function
    :return: None
    """
    # This makes sure that the starting number of coins is random
    coins = randint(10, 1000)

    cur_player = False
    player_name = {False: "Player 1", True: "Player 2"}

    while coins > 0:
        print("Current number of coins:", coins)

        player_input = int(input(f"{player_name[cur_player]}'s Turn: "))

        if valid_move(player_input, coins):
            coins -= player_input
            if coins != 0:
                # change player after each move
                cur_player = not cur_player
        else:
            print("Invalid Move")
    print(player_name[cur_player], "Wins!")


if __name__ == "__main__":
    reset = "y"
    while reset == "y":
        main_loop()
        reset = input("Want to play again? y/n: ").lower()
    else:
        print("Good Bye!")
