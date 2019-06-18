from lifegame import LifeGame
import time
import os
import tkinter

def main():
    def Start(event):
        #エントリーの中身を削除
        seed = EditBox.get()
        EditBox.delete(0, tkinter.END)



    root = tkinter.Tk()
    root.title("Life Game")
    root.geometry("600x400")

    SeedLabel = tkinter.Label(text='seed値=')
    SeedLabel.place(x=40, y=10)

    EditBox = tkinter.Entry(width=10)
    EditBox.place(x=100, y=10)

    StartButton = tkinter.Button(text='Start', width=10)
    StartButton.bind("<Button-1>",Start)
    StartButton.place(x=10, y=50)
    StopButton = tkinter.Button(text='Stop', width=10)
    StopButton.place(x=110, y=50)
    ResetButton = tkinter.Button(text='Reset', width=10)
    ResetButton.place(x=210, y=50)

    LifeGameView = tkinter.Label(text="", width=100, )

    root.mainloop()

if __name__ == "__main__":
    main()