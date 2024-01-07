import random


class Artificial_Intelligence:

    def __init__(self, my_board):

        self.board = my_board
        self.X = 'X'
        self.O = 'O'
        self.EMPTY = ' '

        self.AI_Row = None
        self.AI_Column = None

        self.AI_Run()

    def get_row(self):

        return self.AI_Row

    def get_column(self):

        return self.AI_Column

    # ---------------------------------------------------Пытаемся выиграть---------------------------------------------------
    def Can_Fill_Row(self):

        for n in range(3):
            if self.board[n][0] == self.O and self.board[n][1] == self.O and self.board[n][2] == self.EMPTY:
                self.AI_Row = n
                self.AI_Column = 2
                return True
            elif self.board[n][0] == self.O and self.board[n][1] == self.EMPTY and self.board[n][2] == self.O:
                self.AI_Row = n
                self.AI_Column = 1
                return True
            elif self.board[n][0] == self.EMPTY and self.board[n][1] == self.O and self.board[n][2] == self.O:
                self.AI_Row = n
                self.AI_Column = 0
                return True

    def Can_Fill_Column(self):

        for m in range(3):
            if self.board[0][m] == self.O and self.board[1][m] == self.O and self.board[2][m] == self.EMPTY:
                self.AI_Row = 2
                self.AI_Column = m
                return True
            elif self.board[0][m] == self.O and self.board[1][m] == self.EMPTY and self.board[2][m] == self.O:
                self.AI_Row = 1
                self.AI_Column = m
                return True
            elif self.board[0][m] == self.EMPTY and self.board[1][m] == self.O and self.board[2][m] == self.O:
                self.AI_Row = 0
                self.AI_Column = m
                return True

    def Can_Fill_Main_Diagonal(self):

        if self.board[0][0] == self.O and self.board[1][1] == self.O and self.board[2][2] == self.EMPTY:
            self.AI_Row = 2
            self.AI_Column = 2
            return True
        elif self.board[0][0] == self.O and self.board[1][1] == self.EMPTY and self.board[2][2] == self.O:
            self.AI_Row = 1
            self.AI_Column = 1
            return True
        elif self.board[0][0] == self.EMPTY and self.board[1][1] == self.O and self.board[2][2] == self.O:
            self.AI_Row = 0
            self.AI_Column = 0
            return True

    def Can_Fill_Side_Diagonal(self):

        if self.board[0][2] == self.O and self.board[1][1] == self.O and self.board[2][0] == self.EMPTY:
            self.AI_Row = 2
            self.AI_Column = 0
            return True
        elif self.board[0][2] == self.O and self.board[1][1] == self.EMPTY and self.board[2][0] == self.O:
            self.AI_Row = 1
            self.AI_Column = 1
            return True
        elif self.board[0][2] == self.EMPTY and self.board[1][1] == self.O and self.board[2][0] == self.O:
            self.AI_Row = 0
            self.AI_Column = 2
            return True

    # -------------------------------------------------Пытаемся не проиграть-------------------------------------------------
    def Can_Clog_Row(self):

        for n in range(3):
            if self.board[n][0] == self.X and self.board[n][1] == self.X and self.board[n][2] == self.EMPTY:
                self.AI_Row = n
                self.AI_Column = 2
                return True
            elif self.board[n][0] == self.X and self.board[n][1] == self.EMPTY and self.board[n][2] == self.X:
                self.AI_Row = n
                self.AI_Column = 1
                return True
            elif self.board[n][0] == self.EMPTY and self.board[n][1] == self.X and self.board[n][2] == self.X:
                self.AI_Row = n
                self.AI_Column = 0
                return True

    def Can_Clog_Column(self):

        for m in range(3):
            if self.board[0][m] == self.X and self.board[1][m] == self.X and self.board[2][m] == self.EMPTY:
                self.AI_Row = 2
                self.AI_Column = m
                return True
            elif self.board[0][m] == self.X and self.board[1][m] == self.EMPTY and self.board[2][m] == self.X:
                self.AI_Row = 1
                self.AI_Column = m
                return True
            elif self.board[0][m] == self.EMPTY and self.board[1][m] == self.X and self.board[2][m] == self.X:
                self.AI_Row = 0
                self.AI_Column = m
                return True

    def Can_Clog_Main_Diagonal(self):

        if self.board[0][0] == self.X and self.board[1][1] == self.X and self.board[2][2] == self.EMPTY:
            self.AI_Row = 2
            self.AI_Column = 2
            return True
        elif self.board[0][0] == self.X and self.board[1][1] == self.EMPTY and self.board[2][2] == self.X:
            self.AI_Row = 1
            self.AI_Column = 1
            return True
        elif self.board[0][0] == self.EMPTY and self.board[1][1] == self.X and self.board[2][2] == self.X:
            self.AI_Row = 0
            self.AI_Column = 0
            return True

    def Can_Clog_Side_Diagonal(self):

        if self.board[0][2] == self.X and self.board[1][1] == self.X and self.board[2][0] == self.EMPTY:
            self.AI_Row = 2
            self.AI_Column = 0
            return True
        elif self.board[0][2] == self.X and self.board[1][1] == self.EMPTY and self.board[2][0] == self.X:
            self.AI_Row = 1
            self.AI_Column = 1
            return True
        elif self.board[0][2] == self.EMPTY and self.board[1][1] == self.X and self.board[2][0] == self.X:
            self.AI_Row = 0
            self.AI_Column = 2
            return True

    # ---------------------------------------------------Строим свою линию---------------------------------------------------
    def Can_Build_Row(self):

        for n in range(3):
            if self.board[n][0] == self.O and self.board[n][1] == self.EMPTY and self.board[n][2] == self.EMPTY:
                self.AI_Row = n
                self.AI_Column = 2
                return True
            elif self.board[n][0] == self.EMPTY and self.board[n][1] == self.O and self.board[n][2] == self.EMPTY:
                self.AI_Row = n
                self.AI_Column = 0
                return True
            elif self.board[n][0] == self.EMPTY and self.board[n][1] == self.EMPTY and self.board[n][2] == self.O:
                self.AI_Row = n
                self.AI_Column = 0
                return True

    def Can_Build_Column(self):

        for m in range(3):
            if self.board[0][m] == self.O and self.board[1][m] == self.EMPTY and self.board[2][m] == self.EMPTY:
                self.AI_Row = 2
                self.AI_Column = m
                return True
            elif self.board[0][m] == self.EMPTY and self.board[1][m] == self.O and self.board[2][m] == self.EMPTY:
                self.AI_Row = 0
                self.AI_Column = m
                return True
            elif self.board[0][m] == self.EMPTY and self.board[1][m] == self.EMPTY and self.board[2][m] == self.O:
                self.AI_Row = 0
                self.AI_Column = m
                return True

    def Can_Build_Main_Diagonal(self):

        if self.board[0][0] == self.EMPTY and self.board[1][1] == self.O and self.board[2][2] == self.EMPTY:
            self.AI_Row = 0
            self.AI_Column = 0
            return True

    def Can_Build_Side_Diagonal(self):

        if self.board[0][2] == self.EMPTY and self.board[1][1] == self.O and self.board[2][0] == self.EMPTY:
            self.AI_Row = 2
            self.AI_Column = 0
            return True

    # ---------------------------------------------------Обьеденяем функции--------------------------------------------------
    def Can_Win(self):

        if self.Can_Fill_Row() != True:
            if self.Can_Fill_Column() != True:
                if self.Can_Fill_Main_Diagonal() != True:
                    if self.Can_Fill_Side_Diagonal() != True:
                        return False
        return True

    def Can_Lose(self):

        if self.Can_Clog_Row() != True:
            if self.Can_Clog_Column() != True:
                if self.Can_Clog_Main_Diagonal() != True:
                    if self.Can_Clog_Side_Diagonal() != True:
                        return False
        return True

    def Can_Build(self):

        if self.Can_Build_Side_Diagonal() != True:
            if self.Can_Build_Main_Diagonal() != True:
                if self.Can_Build_Row() != True:
                    if self.Can_Build_Column() != True:
                        return False
        return True

    def Get_Random(self):

        self.AI_Row = 1
        self.AI_Column = 1
        if self.board[self.AI_Row][self.AI_Column] != self.EMPTY:
            if self.board[0][0] == self.EMPTY:
                self.AI_Row = 0
                self.AI_Column = 0
                return
            elif self.board[0][2] == self.EMPTY:
                self.AI_Row = 0
                self.AI_Column = 2
                return
            elif self.board[2][0] == self.EMPTY:
                self.AI_Row = 2
                self.AI_Column = 0
                return
            elif self.board[2][2] == self.EMPTY:
                self.AI_Row = 2
                self.AI_Column = 2
                return
        while self.board[self.AI_Row][self.AI_Column] != self.EMPTY:
            self.AI_Row = random.randint(0, 2)
            self.AI_Column = random.randint(0, 2)

    def AI_Run(self):
        if self.Can_Win() != True:
            if self.Can_Lose() != True:
                if self.Can_Build() != True:
                    self.Get_Random()


'''
if __name__ == "__main__":

    test_board = [['O','X',' '],
                  [' ','O',' '],
                  [' ',' ',' ']]

    AI = Artificial_Intelligence(test_board)

    AI.get_row()
    AI.get_column()
'''
