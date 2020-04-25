from tkinter import *
import tkinter.messagebox
from random import randint

root = Tk()
root.resizable(False, False)
root.title('Game by Yura')


class Playground:
    def __init__(self, n=4):
        if n % 2 == 0:
            self.__n = n                        # number of rows/columns
        else:
            self.__n = n+1

        self.__btns = []
        for i in range(self.__n):
            self.__btns.append([])              # table of buttons (empty)

        self.__size = 2                         # size of a button
        self.__moves = 0                        # number of moves made
        self.__scoreOnLabel = StringVar()       # variable that will be printed on the label
        self.__scoreOnLabel.set(self.__moves)

        self.__up = Frame(root)                 # upper part of the window
        self.__down = Frame(root)               # lower part of the window
        self.__new = Button(self.__up, height=1, width=self.__size*2, text="NEW",
                            bg='green', command=lambda: self.__start())
        self.__esc = Button(self.__up, height=1, width=self.__size*2, text="QUIT",
                            bg='red', command=lambda: self.__close())
        self.__score = Label(self.__up, textvariable=self.__scoreOnLabel, width=self.__size*2)

        for i in range(0, self.__n):
            for j in range(0, self.__n):
                self.__btns[i].append(Button(self.__down, height=self.__size, width=self.__size,
                                             command=lambda row=i, col=j: self.clicked(row, col)))
        self.show()
        self.__start()

    def show(self):     # builds all buttons in a table
        self.__up.grid(row=0, column=0)     #
        self.__new.grid(row=0, column=0)    # All in the upper part
        self.__score.grid(row=0, column=1)  #
        self.__esc.grid(row=0, column=2)    #
        self.__down.grid(row=1, column=0)                   #
        for i in range(0, self.__n):                        # All in the lower part
            for j in range(0, self.__n):                    #
                self.__btns[i][j].grid(row=i, column=j)     #

    def __makeBlack(self, row, col):    # sets cell to a black mode
        el = self.__btns[row][col]
        el['bg'] = 'black'
        el['fg'] = 'white'
        el['activebackground'] = '#555555'
        el['activeforeground'] = 'white'

    def __makeWhite(self, row, col):    # sets cell to a white mode
        el = self.__btns[row][col]
        el['bg'] = 'white'
        el['fg'] = 'black'
        el['activebackground'] = '#cccccc'
        el['activeforeground'] = 'black'

    def __switch(self, row, col):       # switches between white and black
        if self.__btns[row][col]['bg'] == 'white':
            self.__makeBlack(row, col)
        else:
            self.__makeWhite(row, col)

    def __showScore(self):                      # updates score
        self.__scoreOnLabel.set(self.__moves)

    def __changeScore(self):                    # adds number of moves and updates score
        self.__moves += 1
        self.__scoreOnLabel.set(self.__moves)

    def __check(self):                          # checks if user wins
        blacks = 0
        whites = 0
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__btns[i][j]['bg'] == 'white':
                    whites += 1
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__btns[i][j]['bg'] == 'black':
                    blacks += 1
        if blacks == 0 or whites == 0:
            self.__finish()

    def __finish(self):                         # is called when user wins
        answ = tkinter.messagebox.askyesno(title="WINNER", message="Congratulations!\n"
                                                                   "You win with the score of {}.\n"
                                                                   "Do you want to start again?".format(self.__moves))
        if answ:
            self.__moves = 0
            self.__start()
        else:
            root.destroy()

    def clicked(self, row, col):        # switches every element in a row and in a column to another color
        for i in range(self.__n):
            self.__switch(row, i)
            self.__switch(i, col)
        self.__switch(row, col)
        self.__changeScore()
        self.__check()

    def __start(self):                  # starts a new game
        if self.__moves > 0:
            if not tkinter.messagebox.askyesno("New game", "Are you sure you want to start new game?\n"
                                                           "Your progress will be lost."):
                return 0
        self.__moves = 0
        self.__showScore()
        for i in range(self.__n):
            for j in range(self.__n):
                if randint(0, 1) == 0:
                    self.__makeWhite(i, j)
                else:
                    self.__makeBlack(i, j)

    def __close(self):
        if tkinter.messagebox.askyesno("Exit", "Are you sure you want to quit?"):
            root.destroy()


a = Playground(6)
root.mainloop()
