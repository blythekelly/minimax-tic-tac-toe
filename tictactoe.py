from tkinter import *
import customtkinter
import minimax

customtkinter.set_appearance_mode("Dark")

#creating CTk window for app
root = customtkinter.CTk()

#setting window width and height
root.geometry('450x450')


#Creating label
label = customtkinter.CTkLabel(master=root,
                               text="Tic Tac Toe",
                               width=120,
                               height=50,
                               font=("normal", 20),
                               corner_radius=8)
label.place(relx=0.5, rely=0.7, anchor=CENTER)

"""This function handles the clicks on the Tic Tac Toe board.
:param r: the row of the button that was clicked
:param c: the column of the button that was clicked
:return:
"""
depth=9
def clickbutton(r, c):
    buttons[r][c]["text"]="X"
    board[r][c]=-1
    buttons[r][c]['state']=DISABLED

    label = customtkinter.CTkLabel(master=root,
                               text=checkwin(board),
                               width=120,
                               height=25,
                               corner_radius=8)
    label.place(relx=0.5, rely=0.78, anchor=CENTER)

    global depth
    depth-=1
    computerplay()
    depth-=1

    label = customtkinter.CTkLabel(master=root,
                               text=checkwin(board),
                               width=120,
                               height=25,
                               corner_radius=8)
    label.place(relx=0.5, rely=0.78, anchor=CENTER)
    
    

#Button matrix
buttons = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]
 
#Matrix identifying whether buttons are active or inactive
board=[[0,0,0],[0,0,0],[0,0,0]]
 

#Creating the tic tac toe board
root.grid_columnconfigure((0, 1, 2), weight=1)
for i in range(3):
    for j in range(3):                                 
        buttons[i][j] = Button(height = 4, width = 6, font = ("Normal", 20),
                        command = lambda r = i, c = j : clickbutton(r,c))
        buttons[i][j].grid(row = i, column = j, sticky='NESW')


#This function calls the Minimax algorithm to perform the computer's play.
def computerplay():
    global depth
    bestmove=minimax.minimax(board, depth, 1)
    buttons[bestmove[0]][bestmove[1]]['text']="O"
    buttons[bestmove[0]][bestmove[1]]['state']=DISABLED
    board[bestmove[0]][bestmove[1]]=1

#This function checks for a win and updates the label to declare the winner or a draw.
def checkwin(b):
    score=minimax.evaluate(b)
    if score==10:
        return 'Computer won!'
    elif score==-10:
        return 'You won!'
    elif minimax.game_over(b):
        return "It's a draw."
    else:
        return 'Player vs. Computer'

#This defines the reset game button and clears all Tic Tac Toe buttons.
def reset():
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text']=''
            buttons[i][j]['state']=ACTIVE
            board[i][j]=0
    global depth
    depth=8
    
reset_btn=customtkinter.CTkButton(master=root, font = ("Normal", 20),text="Reset game",
                        command = reset)
reset_btn.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
