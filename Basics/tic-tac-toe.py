def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings


def row_winner(board):
    return any(winning_line(row) for row in board)


def column_winner(board):
    return row_winner(zip(*board))


def main_diagonal_winner(board):
    return winning_line(row[i] for i, row in enumerate(board))


def diagonal_winner(board):
    return main_diagonal_winner(board) or main_diagonal_winner(reversed(board))


def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)


def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'


def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))


def make_board(size):
    return [[' '] * size for _ in range(size)]


def prize():                    
    pri = '''
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
               
               '''
    print(pri) 


def print_winner(player):
    print("\n" * 2)
    prize()
    print(f'{player} wins!')


def print_draw():
    print("It's a draw!")


def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    player = player1
    for _ in range(board_size * board_size): #(3*3, 4*4...)
        play_move(board, player)
        
        if winner(board):
            print_winner(player)
            return                  #end program
        if player == player1:
            player = player2
        else:
            player = player1
        print_draw()            #no one has won -> draw


def main(): 
    print("Insert board size")
    board_size = int(input())
    play_game(board_size, 'X', 'O')

main()
