# Piedra Papel y Tijeras version 3

# variables globales


import random

from tkinter import *

import sqlite3

import datetime

root = Tk()


# <------------------ Base de datos --------------------->

# conector de DB
conn = sqlite3.connect('game_records.db')

# cursor DB
c = conn.cursor()

# # creacion de DB
# c.execute("""CREATE TABLE records (
#             player_name text,
#             winns integer,
#             losts integer,
#             date integer
#             )""")



# # commit cambios DB
# conn.commit()

# # cerrar DB
# conn.close()



# Imagenes para los botones
rock_img = PhotoImage(file='rock1.png')
paper_img = PhotoImage(file='paper1.png')
scissors_img = PhotoImage(file='scissors1.png')

rock_label = Label(image=rock_img)
paper_label = Label(image=paper_img)
scissors_label = Label(image=scissors_img)

# configuracion de ventana
root.geometry('610x500')
root.title('Rock, Papel, Scissors GUI')
root.iconbitmap('rock_icon.ico')

# tablero
choice_board = ['Piedra','Papel','Tijeras']

# definicion de check_1 para limpiar valores anteriores en check_game
check_1 = Label(root)

# control de funciones
def game_runs(choice):

    player_choice(choice)
    boot_choice()
    border_color()
    check_game()


# ingreso de opciones de usuario
def player_choice(choice):

    global player

    player = choice - 1
    print(f'Opcion del jugador {player}')


# generador de opciones del boot con el modulo random
def boot_choice():

    global boot

    boot = (random.randrange(1 ,3)) - 1
    print(f'Opcion del boot {boot}')


# cambia el margen de la opcion selecionada para player y boot
def border_color():

    global player
    global boot

    # if player == boot:
    #     match_img = PhotoImage(file='match.png')
    #     match_label = Label(root, image=match_img)
    #     match_label.place(x=100, y=100)

    if player == 0:
        rock_button.config(borderwidth=5)
    elif player == 1:
        paper_button.config(borderwidth=5)
    elif player == 2:
        scissors_button.config(borderwidth=5)


    rock_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    scissors_button.config(state=DISABLED)


    if boot == 0:
        rock_button.config(borderwidth=5)
    elif boot == 1:
        paper_button.config(borderwidth=5)
    elif boot == 2:
        scissors_button.config(borderwidth=5)


contador_player = 0
contador_boot = 0

counter_label = Label(root)


# verificacion de ganador de la partida
def check_game():

    global check_1

    global contador_player
    global contador_boot

    print(choice_board[player], choice_board[boot])

    winner = False
    while not winner:
        # empate
        if player == boot:
            check_1.grid_forget()
            check_1 = Label(root, text=f'{choice_board[player]} empata a {choice_board[boot]}. Nadie gana', font=('Helvetica', 15))
            check_1.grid(row=2, column=1)
            print(f'{choice_board[player]} empata a {choice_board[boot]}. Nadie gana')
            winner = True
        # gana usuario
        elif player == 0 and boot == 2:
            check_1.grid_forget()
            check_1 = Label(root, text=f'{choice_board[player]} gana a {choice_board[boot]}' '\n' 'Eres el ganador', font=('Helvetica', 15), fg='blue')
            check_1.grid(row=2, column=1)
            print(f'{choice_board[player]} gana a {choice_board[boot]}')
            print('Eres el ganador')
            contador_player += 1
            winner = True
        elif player == 1 and boot == 0:
            check_1.grid_forget()
            check_1 = Label(root, text=f'{choice_board[player]} gana a {choice_board[boot]}' '\n' 'Eres el ganador', font=('Helvetica', 15), fg='blue')
            check_1.grid(row=2, column=1)
            print(f'{choice_board[player]} gana a {choice_board[boot]}')
            print('Eres el ganador')
            contador_player += 1
            winner = True
        elif player == 2 and boot == 1:
            check_1.grid_forget()
            check_1 = Label(root, text=f'{choice_board[player]} gana a {choice_board[boot]}' '\n' 'Eres el ganador', font=('Helvetica', 15), fg='blue')
            check_1.grid(row=2, column=1)
            print(f'{choice_board[player]} gana a {choice_board[boot]}')
            print('Eres el ganador')
            contador_player += 1
            winner = True
        # gana boot
        elif boot == 0 and player == 2:
            check_1.grid_forget()
            check_1 = Label(root, text=f'{choice_board[boot]} gana a {choice_board[player]}' '\n' 'Boot gana', font=('Helvetica', 15), fg='red')
            check_1.grid(row=2, column=1)
            print(f'{choice_board[boot]} gana a {choice_board[player]}')
            print('Computadora Gana')
            contador_boot += 1
            winner = True
        elif boot == 1 and player == 0:
            check_1.grid_forget()
            check_1 = Label(root, text=f'{choice_board[boot]} gana a {choice_board[player]}' '\n' 'Boot gana', font=('Helvetica', 15), fg='red')
            check_1.grid(row=2, column=1)
            print(f'{choice_board[boot]} gana a {choice_board[player]}')
            print('Computadora Gana')
            contador_boot += 1
            winner = True
        elif boot == 2 and player == 1:
            check_1.grid_forget()
            check_1 = Label(root, text=f'{choice_board[boot]} gana a {choice_board[player]}' '\n' 'Boot gana', font=('Helvetica', 15), fg='red')
            check_1.grid(row=2, column=1)
            print(f'{choice_board[boot]} gana a {choice_board[player]}')
            print('Computadora Gana')
            contador_boot += 1
            winner = True
        
    counter()


def counter():
    
    global contador_player
    global contador_boot
    global counter_label

    counter_label.grid_forget()

    counter_label = Label(root, text=f'{contador_player}/{contador_boot}', font=('Helvetica', 10))
    counter_label.grid(row=3, column=1)

    print(f'contador de player {contador_player}')
    print(f'contador de boot {contador_boot}')


# resetea los valores de la partida 
def reset_game():

    global check_1
    global contador_player
    global contador_boot
    global counter_label    

    # borra los border selectores
    rock_button.config(borderwidth=0)
    paper_button.config(borderwidth=0)
    scissors_button.config(borderwidth=0)

    # elimina el label de ganador
    check_1.grid_forget()

    rock_button.config(state=ACTIVE)
    paper_button.config(state=ACTIVE)
    scissors_button.config(state=ACTIVE)

    if contador_player == 2:
        contador_player = 0
        contador_boot = 0
        counter_label.grid_forget()

    elif contador_boot == 2:
        contador_player = 0
        contador_boot = 0
        counter_label.grid_forget()



# labels y botenes
welcome_label = Label(root, text=
""" Bienvenido al juego de Piedra, Papel y TIjeras V3.
Mi Primer Programa hecho con tkinter.
Bare with me!
Enjoy

Pick a choice""", font=('Helvetica', 10))

# botones de control
rock_button = Button(root, image=rock_img, command=lambda: game_runs(1), borderwidth=0)
paper_button = Button(root, image=paper_img, command=lambda: game_runs(2), borderwidth=0)
scissors_button = Button(root, image=scissors_img, command=lambda: game_runs(3), borderwidth=0)


# boton para cerrar la ventana
quit_button = Button(root, text='Quit', font=('Helvetica', 10), command=root.quit)

# resetea la partida
reset_button = Button(root, text='Reset', font=('Helvetica', 10), command=reset_game)

# game record
records_button = Button(root, text='Records', font=('Helvetica', 10)) 

# display on grid
welcome_label.grid(row=0, column=1) 

rock_button.grid(row=1, column=0, padx=5, pady=20)
paper_button.grid(row=1, column=1, padx=5, pady=20)
scissors_button.grid(row=1, column=2, padx=5, pady=20)

quit_button.place(x=565, y=460)

reset_button.place(x=520, y=460)

records_button.place(x=10, y=460)

root.mainloop()
