
class TicTacToe():
    # def print_board(self, board):
    #     for row in board:
    #         print(" | ".join(row))
    #         print("-" * 9)

    def check_win(self, board, player):
        win_conditions = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]]
        ]
        return [player, player, player] in win_conditions

    def check_tie(self, board):
        calculation = [board[row][col] != " " for row in range(3) for col in range(3)]
        result = all(calculation)
        # print(calculation)
        return result

    # def get_move(self, player, board):
    #     while True:
    #         try:
    #             move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    #             if move < 0 or move > 8:
    #                 print("Invalid move. Please choose a number between 1 and 9.")
    #             elif board[move // 3][move % 3] != " ":
    #                 print("This space is already taken. Please choose another space.")
    #             else:
    #                 return move
    #         except ValueError:
    #             print("Invalid input. Please enter a number.")

    def play_game(self, current_player, move, board = 0):
        if board == 0:
            board = [[" " for _ in range(3)] for _ in range(3)]
        else: 
            board = board
      
        end_game = False
        result = False
        # self.print_board(board)
        # move = self.get_move(current_player, board)
        board[move // 3][move % 3] = current_player
        
        if self.check_win(board, current_player):
            # self.print_board(board)
            end_game = True
            result = True
            # print(f"Player {current_player} wins!")
            
        elif self.check_tie(board):
            # self.print_board(board)
            end_game = True
            result = False
            # print("It's a tie!")
            
        return board, end_game, result