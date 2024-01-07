# Класы
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton
from menu import Artificial_Intelligence

gameType = 2
score = 0


# Родительский клас окна
class Window:

    def __init__(self, width, height, title, icon):
        self.win = Tk()
        self.win.title(title)
        self.win.geometry(f"{width}x{height}+400+150")
        self.win.resizable(False, False)
        self.win["bg"] = 'medium spring green'
        self.win.protocol("WM_DELETE_WINDOW", self.close_window)

        if icon:
            self.win.iconbitmap(icon)

    def close_window(self):
        self.win.destroy()


# Игровое окно
class MainGame(Window):

    def __init__(self, width=450, height=500, xsize=150, ysize=50,
                 title="Крестики-Нолики", icon=None):

        global gameType
        if gameType == 1:
            title += " - Против Компьютера"
        Window.__init__(self, width, height, title, icon)
        self.box_size = xsize
        self.menu_height = ysize
        self.X = 'X'
        self.O = 'O'
        self.EMPTY = ' '
        self.board = [[self.EMPTY, self.EMPTY, self.EMPTY],
                      [self.EMPTY, self.EMPTY, self.EMPTY],
                      [self.EMPTY, self.EMPTY, self.EMPTY]]
        self.turn = self.X
        self.ai_row = None
        self.ai_column = None
        self.moves = 0
        self.play = True

        self.frame = Frame(master=self.win, bg='green')

        self.btn = [[0 for x in range(3)] for x in range(3)]
        for i in range(3):
            for j in range(3):
                self.btn[i][j] = Button(master=self.frame, text=self.EMPTY,
                                        font="Helvetica 100", bg="black", fg="white",
                                        relief=RIDGE, borderwidth=5,
                                        command=lambda _i=i, _j=j: self.change_btn(_i, _j))

        #       Показывает очередь хода во время игры
        self.lbl_turn = Label(master=self.win, text=f"Сейчас очередь {self.turn} ходить",
                              font="Helvetica 8", bg="black", fg="white", relief=RIDGE)

        #       Выйти в главное меню
        self.btn_quit = Button(master=self.win, text="Выйти в меню", bg="red", fg="black", font="Helvetica 10",
                               relief=RIDGE, borderwidth=5, command=self.quit_to_menu)

        #       Перезапустить игру
        self.btn_again = Button(master=self.win, text="Еще раз", bg="cyan", fg="black",
                                font="Helvetica 10", relief=RIDGE, borderwidth=5, command=self.restart)

    def run(self):

        self.draw_widgets()
        self.win.mainloop()

    def restart(self):

        self.close_window()
        MainGame().run()

    def quit_to_menu(self):

        self.close_window()
        MainMenu().run()

    # Отображает на екране созданые виджеты
    def draw_widgets(self):

        self.frame.place(y=0, x=0, width=self.box_size * 3,
                         height=self.box_size * 3)

        for i in range(3):
            for j in range(3):
                self.btn[i][j].place(y=i * self.box_size, x=j * self.box_size,
                                     width=self.box_size, height=self.box_size)

        self.lbl_turn.place(y=self.box_size * 3, x=self.box_size,
                            width=self.box_size, height=self.menu_height)

    # В конце игры делает игровое поле неактивным,
    # и отображает две новых кнопки для закрытия или перезапуска
    def btn_off(self):

        for x in range(3):
            for y in range(3):
                self.btn[x][y]['state'] = DISABLED
        self.lbl_turn.configure(text=self.EMPTY)
        self.btn_quit.place(y=self.box_size * 3, x=self.box_size * 2,
                            width=self.box_size, height=self.menu_height)
        self.btn_again.place(y=self.box_size * 3, x=0,
                             width=self.box_size, height=self.menu_height)

    # Проверяет заполнение игрового поля
    def over_moves(self):

        if self.moves == 9:
            self.play = False
            messagebox.showinfo('Игра закончена!!!', 'Ничья!!!')

    # Проверяет условия победы
    def isWin(self):

        for i in range(3):

            # Проверка строк
            if self.board[i][0] == self.X and self.board[i][1] == self.X and self.board[i][2] == self.X:
                messagebox.showinfo('Игра закончена!!!', f'{self.X} выиграл!!!')
                self.play = False
                return
            elif self.board[i][0] == self.O and self.board[i][1] == self.O and self.board[i][2] == self.O:
                messagebox.showinfo('Игра закончена!!!', f'{self.O} выиграл')
                self.play = False
                return

            # Проверка столбцов
            elif self.board[0][i] == self.X and self.board[1][i] == self.X and self.board[2][i] == self.X:
                messagebox.showinfo('Игра закончена!!!', f'{self.X} выиграл!!!')
                self.play = False
                return
            elif self.board[0][i] == self.O and self.board[1][i] == self.O and self.board[2][i] == self.O:
                messagebox.showinfo('Игра закончена!!!', f'{self.O} выиграл!!!')
                self.play = False
                return

        # Проверка главной диагонали
        if self.board[0][0] == self.X and self.board[1][1] == self.X and self.board[2][2] == self.X:
            messagebox.showinfo('Игра закончена!!!', f'{self.X} выиграл!!!')
            self.play = False
            return
        elif self.board[0][0] == self.O and self.board[1][1] == self.O and self.board[2][2] == self.O:
            messagebox.showinfo('Игра закончена!!!', f'{self.O} выиграл!!!')
            self.play = False
            return

        # Проверка побочной диагонали
        if self.board[0][2] == self.X and self.board[1][1] == self.X and self.board[2][0] == self.X:
            messagebox.showinfo('Игра закончена!!!', f'{self.X} выиграл!!!')
            self.play = False
            return
        elif self.board[0][2] == self.O and self.board[1][1] == self.O and self.board[2][0] == self.O:
            messagebox.showinfo('Игра закончена!!!', f'{self.O} выиграл!!!')
            self.play = False
            return

        self.over_moves()
        return

    # Генерирует ход Компьютера
    def AI_Choice(self):

        AI = Artificial_Intelligence(self.board)
        self.ai_row = AI.get_row()
        self.ai_column = AI.get_column()

    def AI_Move(self):

        self.AI_Choice()
        self.btn[self.ai_row][self.ai_column]['text'] = self.O
        self.moves += 1
        self.board[self.ai_row][self.ai_column] = self.O
        self.isWin()
        if self.play == False:
            self.btn_off()

    # Выполняет ходы, команда клеток игрового поля
    def change_btn(self, _i, _j):

        if gameType == 2:
            if self.btn[_i][_j]['text'] == self.EMPTY:
                self.btn[_i][_j]['text'] = self.turn
                if self.turn == self.X:
                    self.moves += 1
                    self.board[_i][_j] = self.X
                    self.turn = self.O
                    self.lbl_turn.configure(text=f"Сейчас очередь {self.turn} ходить")
                    self.isWin()
                    if self.play == False:
                        self.btn_off()
                elif self.turn == self.O:
                    self.moves += 1
                    self.board[_i][_j] = self.O
                    self.turn = self.X
                    self.lbl_turn.configure(text=f"Сейчас очередь {self.turn} ходить")
                    self.isWin()
                    if self.play == False:
                        self.btn_off()
            else:
                messagebox.showinfo('Клетка занята!!!', 'Выберите пустую клетку')

        elif gameType == 1:
            if self.btn[_i][_j]['text'] == self.EMPTY:
                self.btn[_i][_j]['text'] = self.X
                self.moves += 1
                self.board[_i][_j] = self.X
                self.isWin()
                if self.play == False:
                    self.btn_off()
                    return
                self.AI_Move()
            else:
                messagebox.showinfo('Клетка занята!!!', 'Выберите пустую клетку')


# Главное меню
class MainMenu(Window):

    def __init__(self, width=400, height=300, xsize=200, ysize=50, title="Меню", icon=None):
        Window.__init__(self, width, height, title, icon)
        self.btn_width = xsize
        self.btn_height = ysize
        self.win["bg"] = 'dodger blue'
        self.btn_play = Button(master=self.win, text="Играть",
                               font="Helvetica 20", bg="medium violet red", fg="white",
                               relief=RIDGE, borderwidth=5, command=self.click_play)

        self.btn_options = Button(master=self.win, text="Настройки",
                                  font="Helvetica 20", bg="medium violet red", fg="white",
                                  relief=RIDGE, borderwidth=5, command=self.click_options)

        self.btn_exit = Button(master=self.win, text="Выйти из игры",
                               font="Helvetica 20", bg="medium violet red", fg="white",
                               relief=RIDGE, borderwidth=5, command=self.close_window)

    def run(self):
        self.draw_widgets()
        self.win.mainloop()

    def restart(self):
        self.win.destroy()
        MainMenu().run()

    def draw_widgets(self):
        self.btn_play.place(x=self.btn_width / 2, y=self.btn_height,
                            width=self.btn_width, height=self.btn_height)
        self.btn_options.place(x=self.btn_width / 2, y=(self.btn_height + 10) * 2,
                               width=self.btn_width, height=self.btn_height)
        self.btn_exit.place(x=self.btn_width / 2, y=(self.btn_height + 10) * 3,
                            width=self.btn_width, height=self.btn_height)

    def click_play(self):
        self.close_window()
        MainGame().run()

    def click_options(self):
        self.close_window()
        Options().run()


class Options(Window):

    def __init__(self, width=400, height=300, xsize=200, ysize=50, title="Настройки", icon=None):

        Window.__init__(self, width, height, title, icon)
        self.main_width = width
        self.main_height = height
        self.widgets_width = xsize
        self.widgets_height = ysize
        self.win["bg"] = 'dodger blue'
        self.selected = IntVar()
        self.selected.set(gameType)
        self.btn_quit = Button(master=self.win, text="Выбрать и выйти", bg="cyan",
                               fg="black", font="Helvetica 10", relief=RIDGE,
                               borderwidth=5, command=self.select_and_quit)
        # game type - game versus computer
        self.rad_gt_gvc = Radiobutton(master=self.win, text="Против Компьютера",
                                      value=1, variable=self.selected)
        # game type - game for two
        self.rad_gt_gft = Radiobutton(master=self.win, text="Для двоих",
                                      value=2, variable=self.selected)

    def run(self):

        self.draw_widgets()
        self.win.mainloop()

    def select_and_quit(self):

        global gameType
        gameType = self.selected.get()
        if gameType == 1:
            messagebox.showinfo('Тип игры изменен', 'Игровой тип = Против Компьютера')
        elif gameType == 2:
            messagebox.showinfo('Тип игры изменен', 'Игровой тип = Для двоих игроков')
        self.close_window()
        MainMenu().run()

    def draw_widgets(self):

        self.btn_quit.place(y=self.main_height - self.widgets_height - 10,
                            x=self.main_width - self.widgets_width - 10,
                            width=self.widgets_width, height=self.widgets_height)
        self.rad_gt_gft.place(x=self.widgets_width / 2, y=self.widgets_height,
                              width=self.widgets_width, height=self.widgets_height)
        self.rad_gt_gvc.place(x=self.widgets_width / 2, y=(self.widgets_height + 10) * 2,
                              width=self.widgets_width, height=self.widgets_height)


if __name__ == "__main__":
    MainMenu().run()
