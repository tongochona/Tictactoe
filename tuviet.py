from tkinter import *
import random
from tkinter import messagebox

# hàm thực hiện sau khi nhấn button
def click_button(row, column):
    global player
    global full
    full+=1

    if button[row][column]['text']=="":
        button[row][column].config(text=player)
        if check_winner(player):
            display_winner(player)
            return
        if player==players[0]: player=players[1]
        else: player=players[0]
        current_turn.config(text=player+" turn")
    if full==9:
        if messagebox.askyesno(title="Tie", message="You continue new game?"):
            new_game()
        else:
            quit()

#Kiểm tra đã có ai chiến thắng chưa
def check_winner(player):

    for row in range(3):
        if button[row][0]["text"]==button[row][1]["text"]==button[row][2]["text"]==player:
            button[row][0].config(bg=background_winner)
            button[row][1].config(bg=background_winner)
            button[row][2].config(bg=background_winner)
            return True
    for column in range(3):
        if button[0][column]["text"]==button[1][column]["text"]==button[2][column]["text"]==player:
            button[0][column].config(bg=background_winner)
            button[1][column].config(bg=background_winner)
            button[2][column].config(bg=background_winner)
            return True
    if button[0][0]["text"] == button[1][1]["text"] == button[2][2]["text"] == player:
        button[0][0].config(bg=background_winner)
        button[1][1].config(bg=background_winner)
        button[2][2].config(bg="green")
        return True
    if button[0][2]["text"] == button[1][1]["text"] == button[2][0]["text"] == player:
        button[2][0].config(bg=background_winner)
        button[1][1].config(bg=background_winner)
        button[2][0].config(bg=background_winner)
        return True
    return False

#hiển thị thông báo chiến thắng
def display_winner(player):
    current_turn.config(text=player + " win")
    answer=messagebox.askyesno(title=player+ "win", message="You continue new game?")
    if answer:
        new_game()
    else: quit()

#game mới
def new_game():
    global full
    full=0
    player = random.choice(players)
    current_turn.config(text="Start")
    for row in range(3):
        for column in range(3):
            button[row][column] = Button(frame, text="", font=("consolas", 20), width=9, height=4,
                                         command=lambda row=row, column=column: click_button(row, column))
            button[row][column].grid(row=row, column=column)


window= Tk()
window.geometry("500x500")

players=["x","o"]
player=random.choice(players)
background_winner="green"
current_turn=Label(text="Start", font=("consolas", 25))
current_turn.pack()

button=[[None, None, None],
        [None, None, None],
        [None, None, None]]
frame=Frame(window)
frame.pack()
new_game()
window.mainloop()
