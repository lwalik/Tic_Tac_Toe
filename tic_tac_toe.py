class Board:

    def __init__(self):
        self.symbolsOnBoard = {
            "row1": [" ", " ", " "],
            "row2": [" ", " ", " "],
            "row3": [" ", " ", " "]
        }

        self.currentBoard = ""

        self.symbols = ["X", "O"]
        self.variable = 0
        self.moveCounter = 0
        self.firstPlayerInNextRound = 0

    def check_who_will_start(self):
        if self.firstPlayerInNextRound == 0:
            self.variable = 1
        else:
            self.variable = 0

    def check_symbol(self):
        if self.variable == 0:
            self.variable = 1
        else:
            self.variable = 0

    def move(self):
        pick = input("What's your move (example: A1, B2):")
        pickRow = pick[0]
        pickColumn = int(pick[1])

        if self.moveCounter == 0:
            self.firstPlayerInNextRound = self.variable

        self.moveCounter += 1

        if pickRow.upper() == "A":
            if self.symbolsOnBoard["row1"][pickColumn - 1] == " ":
                self.symbolsOnBoard["row1"][pickColumn -
                                            1] = self.symbols[self.variable]
                self.check_symbol()
            else:
                print(28 * "#")
                print("This field is already taken.")

        elif pickRow.upper() == "B":
            if self.symbolsOnBoard["row2"][pickColumn - 1] == " ":
                self.symbolsOnBoard["row2"][pickColumn -
                                            1] = self.symbols[self.variable]
                self.check_symbol()
            else:
                print(28 * "#")
                print("This field is already taken.")
        elif pickRow.upper() == "C":
            if self.symbolsOnBoard["row3"][pickColumn - 1] == " ":
                self.symbolsOnBoard["row3"][pickColumn -
                                            1] = self.symbols[self.variable]
                self.check_symbol()
            else:
                print(28 * "#")
                print("This field is already taken.")

    def check_is_it_full(self):
        if " " not in self.symbolsOnBoard["row1"] and " " not in self.symbolsOnBoard["row2"] and " " not in self.symbolsOnBoard["row3"]:
            return True
        else:
            return False

    def restart_game(self):
        self.symbolsOnBoard = {
            "row1": [" ", " ", " "],
            "row2": [" ", " ", " "],
            "row3": [" ", " ", " "]
        }
        self.moveCounter = 0

    def check_x_win(self):
        if self.symbolsOnBoard["row1"][0] == "X" and self.symbolsOnBoard["row1"][1] == "X" and self.symbolsOnBoard["row1"][2] == "X":
            return True
        elif self.symbolsOnBoard["row2"][0] == "X" and self.symbolsOnBoard["row2"][1] == "X" and self.symbolsOnBoard["row2"][2] == "X":
            return True
        elif self.symbolsOnBoard["row3"][0] == "X" and self.symbolsOnBoard["row3"][1] == "X" and self.symbolsOnBoard["row3"][2] == "X":
            return True
        elif self.symbolsOnBoard["row1"][0] == "X" and self.symbolsOnBoard["row2"][0] == "X" and self.symbolsOnBoard["row3"][0] == "X":
            return True
        elif self.symbolsOnBoard["row1"][1] == "X" and self.symbolsOnBoard["row2"][1] == "X" and self.symbolsOnBoard["row3"][1] == "X":
            return True
        elif self.symbolsOnBoard["row1"][2] == "X" and self.symbolsOnBoard["row2"][2] == "X" and self.symbolsOnBoard["row3"][2] == "X":
            return True
        elif self.symbolsOnBoard["row1"][0] == "X" and self.symbolsOnBoard["row2"][1] == "X" and self.symbolsOnBoard["row3"][2] == "X":
            return True
        elif self.symbolsOnBoard["row1"][2] == "X" and self.symbolsOnBoard["row2"][1] == "X" and self.symbolsOnBoard["row3"][0] == "X":
            return True
        else:
            return False

    def check_o_win(self):
        if self.symbolsOnBoard["row1"][0] == "O" and self.symbolsOnBoard["row1"][1] == "O" and self.symbolsOnBoard["row1"][2] == "O":
            return True
        elif self.symbolsOnBoard["row2"][0] == "O" and self.symbolsOnBoard["row2"][1] == "O" and self.symbolsOnBoard["row2"][2] == "O":
            return True
        elif self.symbolsOnBoard["row3"][0] == "O" and self.symbolsOnBoard["row3"][1] == "O" and self.symbolsOnBoard["row3"][2] == "O":
            return True
        elif self.symbolsOnBoard["row1"][0] == "O" and self.symbolsOnBoard["row2"][0] == "O" and self.symbolsOnBoard["row3"][0] == "O":
            return True
        elif self.symbolsOnBoard["row1"][1] == "O" and self.symbolsOnBoard["row2"][1] == "O" and self.symbolsOnBoard["row3"][1] == "O":
            return True
        elif self.symbolsOnBoard["row1"][2] == "O" and self.symbolsOnBoard["row2"][2] == "O" and self.symbolsOnBoard["row3"][2] == "O":
            return True
        elif self.symbolsOnBoard["row1"][0] == "O" and self.symbolsOnBoard["row2"][1] == "O" and self.symbolsOnBoard["row3"][2] == "O":
            return True
        elif self.symbolsOnBoard["row1"][2] == "O" and self.symbolsOnBoard["row2"][1] == "O" and self.symbolsOnBoard["row3"][0] == "O":
            return True
        else:
            return False

    def __str__(self):
        self.currentBoard = f"""
              1   2   3

        A     {self.symbolsOnBoard["row1"][0]} | {self.symbolsOnBoard["row1"][1]} | {self.symbolsOnBoard["row1"][2]}
             ---|---|---
        B     {self.symbolsOnBoard["row2"][0]} | {self.symbolsOnBoard["row2"][1]} | {self.symbolsOnBoard["row2"][2]}
             ---|---|---
        C     {self.symbolsOnBoard["row3"][0]} | {self.symbolsOnBoard["row3"][1]} | {self.symbolsOnBoard["row3"][2]}
        """
        return self.currentBoard


board = Board()
print(board)
scoreX = 0
scoreO = 0

while True:
    board.move()

    print(board)

    if board.check_x_win():
        scoreX += 1
        print(10 * " ", "Player X Win this round\n")
        choice_about_next_game = input(
            "Do you want start next game? (Y/N): ")
        if choice_about_next_game.upper() == "Y":
            board.check_who_will_start()
            board.restart_game()
            print(board)
        else:
            break
    if board.check_o_win():
        scoreO += 1
        print(10 * " ", "Player O Win this round\n")
        choice_about_next_game = input(
            "Do you want start next next game? (Y/N): ")
        if choice_about_next_game.upper() == "Y":
            board.check_who_will_start()
            board.restart_game()
            print(board)
        else:
            break

    if board.check_is_it_full():
        print("It's a Draw!")
        choice_about_next_game = input(
            "Do you want start next next game? (Y/N): ")
        if choice_about_next_game.upper() == "Y":
            board.check_who_will_start()
            board.restart_game()
            print(board)
        else:
            break

if scoreX > scoreO:
    print("Player X Won the game!")
    print(10 * " ", f"|Score|")
    print(f"Player X scored {scoreX} points.")
    print(f"Player O scored {scoreO} points.")
elif scoreO > scoreX:
    print("Player O Won the game!")
    print(10 * " ", f"|Score|")
    print(f"Player X scored {scoreX} points.")
    print(f"Player O scored {scoreO} points.")
else:
    print("It's a Draw in game!")
    print(10 * " ", f"|Score|")
    print(f"Player X scored {scoreX} points.")
    print(f"Player O scored {scoreO} points.")
