def check_if_possible(x, n):
    """
    Checks if play x is possible
    if its possible apply it then return true
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


coins = 100
cur_player = False
player_name = {False: "Player 1", True: "Player 2"}
while coins > 0:
    print("Current number of coins:", coins)
    player_input = int(input(f"{player_name[cur_player]}'s Turn: "))
    if check_if_possible(player_input, coins):
        coins -= player_input
        if coins != 0:
            # reverse player after each move
            cur_player = not cur_player
    else:
        print("Invalid Move")
print(player_name[cur_player], "Wins!")
