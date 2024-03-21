import numpy, color_print

class Board:
    def __init__(self, rows: int, columns: int) -> None:
        self.board = list(map(lambda iterable: list(iterable), numpy.zeros(rows*columns, dtype=int).reshape(rows, columns)))
        self.row_length = columns
        self.column_height = rows

        for row in self.board:
            for n in row:
                print(n, end="  ")
            print("")

    def place(self, pos: int, player: int) -> None:
        if pos > len(self.board) or pos < 0:
            raise ValueError("Position is outside the board")

        for i in range(len(self.board) - 1, -1, -1):
            if self.board[i][pos] == 0:
                self.board[i][pos] = player
                
                return None
        
        raise Exception("Collumn is full")
    
    def check_winner(self) -> "list[bool, int]":
        if 0 not in self.board[0]:
            return [True, 0]

        for row in self.board:
            nums_in_a_row = 0
            player_checked_row = 0

            for i in range(self.row_length - 1, 0, -1):
                if row[i] != 0 and row[i] == row[i - 1]:
                    nums_in_a_row += 1 if nums_in_a_row > 0 else 2
                    player_checked_row = row[i]

                    if nums_in_a_row >= 4:
                        return [True, player_checked_row]
                else:
                    nums_in_a_row = 0

        nums_in_column = 0
        player_checked_column = 0
        for i in range(self.row_length):
            for n in range(self.column_height - 1, 0, -1):
                if self.board[n][i] != 0 and self.board[n][i] == self.board[n - 1][i]:
                    nums_in_column += 1 if nums_in_column > 0 else 2
                    player_checked_column = self.board[n][i]
                
                    if nums_in_column >= 4:
                        return [True, player_checked_column]
                else:
                    nums_in_column = 0

        #TODO: Find way to make it modular, currently only works for 6x7 grid
        #TODO: Find a formula for the amount of diagonals in a 2D grid
        """Ugly ass code, but it works!"""
        for i in range(-5, 6):
            nums_in_diag = 0
            player_checked_diag = 0

            diagonal = numpy.diagonal(self.board, i)

            for n in range(len(diagonal) - 1, 0, -1):
                if diagonal[n] != 0 and diagonal[n] == diagonal[n - 1]:
                    nums_in_diag += 1 if nums_in_diag > 0 else 2
                    player_checked_diag = diagonal[n]

                    if nums_in_diag >= 4:
                        return [True, player_checked_diag]
                else:
                    nums_in_diag = 0

        for i in range(-5, 6):
            nums_in_diag = 0
            player_checked_diag = 0

            diagonal = numpy.diagonal(numpy.fliplr(self.board), i)

            for n in range(len(diagonal) - 1, 0, -1):
                if diagonal[n] != 0 and diagonal[n] == diagonal[n - 1]:
                    nums_in_diag += 1 if nums_in_diag > 0 else 2
                    player_checked_diag = diagonal[n]

                    if nums_in_diag >= 4:
                        return [True, player_checked_diag]
                else:
                    nums_in_diag = 0

        return [False, 0]

playing_board = Board(6, 7)
won = False
player = 1

while not won:
    print("\n", f"It is player {player}'s turn", sep="")

    pos = int(input("Place your token in collumn: ")) - 1

    try:
        playing_board.place(pos, player)
    except ValueError:
        color_print.print_red("Position is outside the board, try again")
    except:
        color_print.print_red("Collumn is full, try again")
    finally:
        won, player_won = playing_board.check_winner()

        for row in playing_board.board:
            for n in row:
                if n == 1:
                    color_print.print_blue(n, end="  ")
                elif n == 2:
                    color_print.print_yellow(n, end="  ")
                else:
                    print(n, end="  ")
            print("")

        if won and player_won != 0:
            color_print.print_green(f'player {player_won} has won the game')
        elif won and player_won == 0:
            color_print.print_yellow("The players have tied")

        player = 1 if player == 2 else 2