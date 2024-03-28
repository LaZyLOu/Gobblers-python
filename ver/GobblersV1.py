###       Morpion type Gobblers
import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, index, player):
        self.board[row][col] = [index]

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True 
    
    def is_spot_taken(self, row, col, player):
        if self.fix_spot(row - 1, col - 1, player) == 'X' or 'O' : #and self.fix_spot(row - 1, col - 1, player) != '-':
                row, col = list(
                    map(int, input("Spot already taken. Enter row and column numbers to fix spot: ").split()))
                print()
                self.is_spot_taken(row, col, player)
        else: return True
        
    def swap_player_turn(self, player):
        return '2' if player == '1' else '1'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = '2' if self.get_random_first_player() == 1 else '1'
        SizeP1 = [1, 2, 3]
        SizeP2 = ['a', 'b', 'c']
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print() 
            if player == '1':
                print(SizeP1)
                index = int(input("Which size do you want to play ?"))
                print (self.board[row][col])
                
            if player == '2':
                index = int(input("Which size do you want to play ?"))
                for index in SizeP2 :
                    self.fix_spot(row - 1, col - 1,index , player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
