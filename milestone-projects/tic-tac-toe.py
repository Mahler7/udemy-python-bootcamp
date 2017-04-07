

def game_board():
    print('Welcome to the Tic-Tac-Toe game')
    print("Enter a number that's available on the board when it's your turn.")

    board = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    game_over = False
    
    player1_marker = 'X'
    player2_marker = 'O'

    while game_over == False:
        player1_move = None
        correct_move1 = False
        while correct_move1 == False:
            player1_move = int(input("Player 1's Turn: "))
            if board[(player1_move) - 1][0] == player1_move:
                board[(player1_move) - 1][0] = player1_marker
                correct_move1 = True
            elif board[(player1_move) - 1][0] != player1_move:
                print("That spot has been taken, select another: ")
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

        if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
            print('Player 1 Wins')
            game_over = True
            break
        elif board[3][0] == 'X' and board[4][0] == 'X' and board[5][0] == 'X':
            print('Player 1 Wins')
            game_over = True
            break
        elif board[6][0] == 'X' and board[7][0] == 'X' and board[8][0] == 'X':
            print('Player 1 Wins')
            game_over = True
            break
        elif board[0][0] == 'X' and board[3][0] == 'X' and board[6][0] == 'X':
            print('Player 1 Wins')
            game_over = True
            break
        elif board[1][0] == 'X' and board[4][0] == 'X' and board[7][0] == 'X':
            print('Player 1 Wins')
            game_over = True
            break
        elif board[2][0] == 'X' and board[5][0] == 'X' and board[8][0] == 'X':
            print('Player 1 Wins')
            game_over = True
            break
        elif board[0][0] == 'X' and board[4][0] == 'X' and board[8][0] == 'X':
            print('Player 1 Wins')
            game_over = True
            break
        elif board[2][0] == 'X' and board[4][0] == 'X' and board[6][0] == 'X':
            print('Player 1 Wins')
            game_over = True
            break

        player2_move = None
        correct_move2 = False
        while correct_move2 == False:
            player2_move = int(input("Player 2's Turn: "))
            if board[(player2_move) - 1][0] == player2_move:
                board[(player2_move) - 1][0] = player2_marker
                correct_move2 = True
            elif board[(player2_move) - 1][0] != player2_move:
                print("That spot has been taken, select another: ")
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

        if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
            print('Player 2 Wins')
            game_over = True
            break
        elif board[3][0] == 'O' and board[4][0] == 'O' and board[5][0] == 'O':
            print('Player 2 Wins')
            game_over = True
            break
        elif board[6][0] == 'O' and board[7][0] == 'O' and board[8][0] == 'O':
            print('Player 2 Wins')
            game_over = True
            break
        elif board[0][0] == 'O' and board[3][0] == 'O' and board[6][0] == 'O':
            print('Player 2 Wins')
            game_over = True
            break
        elif board[1][0] == 'O' and board[4][0] == 'O' and board[7][0] == 'O':
            print('Player 2 Wins')
            game_over = True
            break
        elif board[2][0] == 'O' and board[5][0] == 'O' and board[8][0] == 'O':
            print('Player 2 Wins')
            game_over = True
            break
        elif board[0][0] == 'O' and board[4][0] == 'O' and board[8][0] == 'O':
            print('Player 2 Wins')
            game_over = True
            break
        elif board[2][0] == 'O' and board[4][0] == 'O' and board[6][0] == 'O':
            print('Player 2 Wins')
            game_over = True
            break
        else:
            game_over = False

        play_count = 0
        for i in board:
            for j in i:
                if j == 'X' or j == 'O':
                    play_count = play_count + 1

        if play_count == 9:
            print('Draw')
            game_over = True
            break

# def game_intro():
#     print('Welcome to the Tic-Tac-Toe game')
#     print("Enter a number that's available on the board when it's your turn.")
#     run_game()

# def run_game():
#     board = game_board()
#     game_over = False
#     while game_over == False:
#         print_game_board(board)
#         player1_moves(board)
#         check_player1_win(board) 
#         check_tie(board)
#         print_game_board(board)
#         player2_moves(board)
#         check_player2_win(board)
        
        
# def player1_moves(board):
#     board = board
#     player1_move = None
#     player1_marker = 'X'
#     player1_check_move(board, player1_move, player1_marker)


# def player1_check_move(board, player1_move, player1_marker):
#     board = board
#     player1_move = player1_move
#     player1_marker = player1_marker
    
#     correct_move1 = False
#     while correct_move1 == False:
#         player1_move = int(input("Player 1's Turn: "))
#         if board[(player1_move) - 1][0] == player1_move:
#             board[(player1_move) - 1][0] = player1_marker
#             correct_move1 = True
#         elif board[(player1_move) - 1][0] != player1_move:
#             print("That spot has been taken, select another: ")
#     return correct_move1

# def check_player1_win(board):
#     if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[3][0] == 'X' and board[4][0] == 'X' and board[5][0] == 'X':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[6][0] == 'X' and board[7][0] == 'X' and board[8][0] == 'X':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[0][0] == 'X' and board[3][0] == 'X' and board[6][0] == 'X':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[1][0] == 'X' and board[4][0] == 'X' and board[7][0] == 'X':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[2][0] == 'X' and board[5][0] == 'X' and board[8][0] == 'X':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[0][0] == 'X' and board[4][0] == 'X' and board[8][0] == 'X':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[2][0] == 'X' and board[4][0] == 'X' and board[6][0] == 'X':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     else:
#         game_over = False
#         return False

# def player2_moves(board):
#     board = board
#     player2_move = None
#     player2_marker = 'X'
#     player2_check_move(board, player2_move, player2_marker)


# def player2_check_move(board, player2_move, player2_marker):
#     board = board
#     player2_move = player2_move
#     player2_marker = player2_marker
    
#     correct_move1 = False
#     while correct_move1 == False:
#         player2_move = int(input("Player 1's Turn: "))
#         if board[(player2_move) - 1][0] == player2_move:
#             board[(player2_move) - 1][0] = player2_marker
#             correct_move1 = True
#         elif board[(player2_move) - 1][0] != player2_move:
#             print("That spot has been taken, select another: ")

# def check_player2_win(board):
#     if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[3][0] == 'O' and board[4][0] == 'O' and board[5][0] == 'O':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[6][0] == 'O' and board[7][0] == 'O' and board[8][0] == 'O':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[0][0] == 'O' and board[3][0] == 'O' and board[6][0] == 'O':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[1][0] == 'O' and board[4][0] == 'O' and board[7][0] == 'O':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[2][0] == 'O' and board[5][0] == 'O' and board[8][0] == 'O':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[0][0] == 'O' and board[4][0] == 'O' and board[8][0] == 'O':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over
#     elif board[2][0] == 'O' and board[4][0] == 'O' and board[6][0] == 'O':
#         print('Player 1 Wins')
#         game_over = True
#         return game_over

# def check_tie(board):
#     board = board
#     play_count = 0
#     for i in board:
#         for j in i:
#             if j == 'X' or j == 'O':
#                 play_count = play_count + 1

#     if play_count == 9:
#         print('Draw')
#         game_over = True
#         return game_over

# def game_board():   
#     board = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
#     return board

# def print_game_board(board):
#     board = board
#     print(board[0], board[1], board[2])
#     print(board[3], board[4], board[5])
#     print(board[6], board[7], board[8])   
       

# def play_game():
#     play = input('Do you want to play tic-tac-toe? y/n: ')
#     if play == 'y':
#         game_intro()
#     else:
#         print('Closing Game')
#         exit()

# play_game()




