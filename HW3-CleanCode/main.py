from game import GoldRush


def play_game():
    print("Welcome to Gold Rush!")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    game = GoldRush(rows, cols)
    game.load_board()
    game.print()

    player1 = 'player1'
    player2 = 'player2'
    while not game.win:
        if player_turn(game, player1):
            game.win = player1
            break
        if player_turn(game, player2):
            game.win = player2


def player_turn(game, player):
    direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
    game.move_player(player, direction)
    game.print()
    if game._check_win(player):
        print(f"{player} wins!")
        return True
    return False


if __name__ == "__main__":
    play_game()