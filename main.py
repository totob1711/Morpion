import customtkinter
import secrets

# Permet d'éviter les erreurs sur la fonction de verification (parce que les pions sont créés au fur et a mesure)
pawns_H1 = None
pawns_H2 = None
pawns_H3 = None
pawns_M1 = None
pawns_M2 = None
pawns_M3 = None
pawns_B1 = None
pawns_B2 = None
pawns_B3 = None

# Variable pour savoir si la partie à été lancé ou non
on_playing = False

# Création d'une liste pour voir les cases remplies ou non 
all_cases = []

# Fonction qui permet de vérifier si l'ordinateur ou le joueur gagne la partie
def verify():
    
    global btn_reinitialiser
    if pawns_H1 == 'X' and pawns_H2 == 'X' and pawns_H3 == 'X':
        informations.delete(0, 'end')
        informations.insert(0, "X à gagné, O à perdu")
    elif pawns_M1 == 'X' and pawns_M2 == 'X' and pawns_M3 == 'X':
        informations.delete(0, 'end')
        informations.insert(0, "X à gagné, O à perdu")
    elif pawns_B1 == 'X' and pawns_B2 == 'X' and pawns_B3 == 'X':
        informations.delete(0, 'end')
        informations.insert(0, "X à gagné, O à perdu")
    elif pawns_H1 == 'X' and pawns_M2 == 'X' and pawns_B3 == 'X':
        informations.delete(0, 'end')
        informations.insert(0, "X à gagné, O à perdu")
    elif pawns_H3 == 'X' and pawns_M2 == 'X' and pawns_B1 == 'X':
        informations.delete(0, 'end')
        informations.insert(0, "X à gagné, O à perdu")
    elif pawns_H1 == 'X' and pawns_M1 == 'X' and pawns_B1 == 'X':
        informations.delete(0, 'end')
        informations.insert(0, "X à gagné, O à perdu")
    elif pawns_H2 == 'X' and pawns_M2 == 'X' and pawns_B2 == 'X':
        informations.delete(0, 'end')
        informations.insert(0, "X à gagné, O à perdu")
    elif pawns_H3 == 'X' and pawns_M3 == 'X' and pawns_B3 == 'X':
        informations.delete(0, 'end')
        informations.insert(0, "X à gagné, O à perdu")
    elif pawns_H1 == 'O' and pawns_H2 == 'O' and pawns_H3 == 'O':
        informations.delete(0, 'end')
        informations.insert(0, "O à gagné, X à perdu")
    elif pawns_M1 == 'O' and pawns_M2 == 'O' and pawns_M3 == 'O':
        informations.delete(0, 'end')
        informations.insert(0, "O à gagné, X à perdu")
    elif pawns_B1 == 'O' and pawns_B2 == 'O' and pawns_B3 == 'O':
        informations.delete(0, 'end')
        informations.insert(0, "O à gagné, X à perdu")
    elif pawns_H1 == 'O' and pawns_M2 == 'O' and pawns_B3 == 'O':
        informations.delete(0, 'end')
        informations.insert(0, "O à gagné, X à perdu")
    elif pawns_H3 == 'O' and pawns_M2 == 'O' and pawns_B1 == 'O':
        informations.delete(0, 'end')
        informations.insert(0, "O à gagné, X à perdu")
    elif pawns_H1 == 'O' and pawns_M1 == 'O' and pawns_B1 == 'O':
        informations.delete(0, 'end')
        informations.insert(0, "O à gagné, X à perdu")
    elif pawns_H2 == 'O' and pawns_M2 == 'O' and pawns_B2 == 'O':
        informations.delete(0, 'end')
        informations.insert(0, "O à gagné, X à perdu")
    elif pawns_H3 == 'O' and pawns_M3 == 'O' and pawns_B3 == 'O':
        informations.delete(0, 'end')
        informations.insert(0, "O à gagné, X à perdu")

# Fonctions qui permet à l'ordinateur de jouer
def laptop_play():
    choose_pawns = secrets.choice(all_cases)
    if choose_pawns == 0:
        while choose_pawns == 0:
            choose_pawns = secrets.choice(all_cases)
    print(choose_pawns)
    choose_pawns.destroy()
    pawns = str(choose_pawns)
    caseNumber = pawns[11:]
    if caseNumber == '1':
        pawns_H1 = customtkinter.CTkLabel(root, text='O', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_H1.place(x=115, y=75)
        pawns_H1 = 'O'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[0] = 0
    elif caseNumber == '2':
        pawns_H2 = customtkinter.CTkLabel(root, text='O', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_H2.place(x=170, y=75)
        pawns_H2 = 'O'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[1] = 0
    elif caseNumber == '3':
        pawns_H3 = customtkinter.CTkLabel(root, text='O', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_H3.place(x=225, y=75)
        pawns_H3 = 'O'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[2] = 0
    elif caseNumber == '4':
        pawns_M1 = customtkinter.CTkLabel(root, text='O', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_M1.place(x=115, y=130)
        pawns_M1 = 'O'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[3] = 0
    elif caseNumber == '5':
        pawns_M2 = customtkinter.CTkLabel(root, text='O', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_M2.place(x=170, y=130)
        pawns_M2 = 'O'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[4] = 0
    elif caseNumber == '6':
        pawns_M3 = customtkinter.CTkLabel(root, text='O', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_M3.place(x=225, y=130)
        pawns_M3 = 'O'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[5] = 0
    elif caseNumber == '7':
        pawns_B1 = customtkinter.CTkLabel(root, text='O', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_B1.place(x=115, y=185)
        pawns_B1 = 'O'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[6] = 0
    elif caseNumber == '8':
        pawns_B2 = customtkinter.CTkLabel(root, text='O', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_B2.place(x=170, y=185)
        pawns_B2 = 'O'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[7] = 0
    elif caseNumber == '9':
        pawns_B3 = customtkinter.CTkLabel(root, text='O', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_B3.place(x=225, y=185)
        pawns_B3 = 'O'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[8] = 0

# Fonctions qui permet de lancer la partie
def start():

    btn_start.destroy()
    global on_playing
    on_playing = True
    
    global player
    player = 0
    if player%2 == 0:
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
    else:
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à l'ordi de jouer")

# Fonctions qui permettent de poser les pions pour le joueur
def print_pawns_H1():
    
    #Verification du lancement de la partie
    if on_playing == True:
        # Remplacement du bouton par le pion
        btn_H1.destroy() 
        global pawns_H1
        pawns_H1 = customtkinter.CTkLabel(root, text='X', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_H1.place(x=115, y=75)
        pawns_H1 = 'X'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[0] = 0
        laptop_play()
    else:
        pass
    verify()

def print_pawns_H2():
    if on_playing == True:
        btn_H2.destroy()
        global pawns_H2
        pawns_H2 = customtkinter.CTkLabel(root, text='X', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_H2.place(x=170, y=75)
        pawns_H2 = 'X'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[1] = 0
        laptop_play()
    else:
        pass
    verify()

def print_pawns_H3():
    
    if on_playing == True:
        btn_H3.destroy()
        global pawns_H3
        pawns_H3 = customtkinter.CTkLabel(root, text='X', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_H3.place(x=225, y=75)
        pawns_H3 = 'X'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[2] = 0
        laptop_play()
    else:
        pass
    verify()

def print_pawns_M1():
    
    if on_playing == True:
        btn_M1.destroy()
        global pawns_M1
        pawns_M1 = customtkinter.CTkLabel(root, text='X', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_M1.place(x=115, y=130)
        pawns_M1 = 'X'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[3] = 0
        laptop_play()
    else:
        pass
    verify()

def print_pawns_M2():
    
    if on_playing == True:
        btn_M2.destroy()
        global pawns_M2
        pawns_M2 = customtkinter.CTkLabel(root, text='X', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_M2.place(x=170, y=130)
        pawns_M2 = 'X'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[4] = 0
        laptop_play()
    else:
        pass
    verify()

def print_pawns_M3():
    
    if on_playing == True:
        btn_M3.destroy()
        global pawns_M3
        pawns_M3 = customtkinter.CTkLabel(root, text='X', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_M3.place(x=225, y=130)
        pawns_M3 = 'X'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[5] = 0
        laptop_play()
    else:
        pass 
    verify()   

def print_pawns_B1():
    
    if on_playing == True:
        btn_B1.destroy()
        global pawns_B1
        pawns_B1 = customtkinter.CTkLabel(root, text='X', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_B1.place(x=115, y=185)
        pawns_B1 = 'X'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[6] = 0
        laptop_play()
    else:
        pass
    verify()

def print_pawns_B2():
    
    if on_playing == True:
        btn_B2.destroy()
        global pawns_B2
        pawns_B2 = customtkinter.CTkLabel(root, text='X', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_B2.place(x=170, y=185)
        pawns_B2 = 'X'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[7] = 0
        laptop_play()
    else:
        pass
    verify()

def print_pawns_B3():
    
    if on_playing == True:
        btn_B3.destroy()
        global pawns_B3
        pawns_B3 = customtkinter.CTkLabel(root, text='X', font=("Arial",16), bg_color='#323232', fg_color='#323232', text_color='white', width=50, height=50)
        pawns_B3.place(x=225, y=185)
        pawns_B3 = 'X'
        informations.get()
        informations.delete(0, 'end')
        informations.insert(0, "C'est à vous de jouer")
        all_cases[8] = 0
        laptop_play()
    else:
        pass
    verify()

# Creation de l'interface graphique
root = customtkinter.CTk()
root.title("Morpion")
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(400,400)
root.config(background='white')

# Insertion d'un titre de page
title = customtkinter.CTkLabel(root, text='JEU DU MORPION', font=("Arial",24), bg_color='white', fg_color='white', text_color='black')
title.place(x=95, y=20)

# Création du tableau de jeu
lines_color = customtkinter.CTkFrame(root, bg_color='green', fg_color='green', width=160, height=160)
lines_color.place(x=115, y=75)

# Création des boutons qui representent les cases ou nous jouons (H1 = la première case de la ligne du haut, H2 = la deuxième case de la ligne du haut etc)
btn_H1 = customtkinter.CTkButton(root, text="", bg_color='#323232', fg_color='#323232', hover_color='white', width=50, height=50, command=print_pawns_H1)
btn_H1.place(x=115, y=75)
all_cases.append(btn_H1)
btn_H2 = customtkinter.CTkButton(root, text="", bg_color='#323232', fg_color='#323232', hover_color='white', width=50, height=50, command=print_pawns_H2)
btn_H2.place(x=170, y=75)
all_cases.append(btn_H2)
btn_H3 = customtkinter.CTkButton(root, text="", bg_color='#323232', fg_color='#323232', hover_color='white', width=50, height=50, command=print_pawns_H3)
btn_H3.place(x=225, y=75)
all_cases.append(btn_H3)

# Création des boutons qui representent les cases ou nous jouons (M1 = la première case de la ligne du milieu, M2 = la deuxième case de la ligne du milieu etc)
btn_M1 = customtkinter.CTkButton(root, text="", bg_color='#323232', fg_color='#323232', hover_color='white', width=50, height=50, command=print_pawns_M1)
btn_M1.place(x=115, y=130)
all_cases.append(btn_M1)
btn_M2 = customtkinter.CTkButton(root, text="", bg_color='#323232', fg_color='#323232', hover_color='white', width=50, height=50, command=print_pawns_M2)
btn_M2.place(x=170, y=130)
all_cases.append(btn_M2)
btn_M3 = customtkinter.CTkButton(root, text="", bg_color='#323232', fg_color='#323232', hover_color='white', width=50, height=50, command=print_pawns_M3)
btn_M3.place(x=225, y=130)
all_cases.append(btn_M3)

# Création des boutons qui representent les cases ou nous jouons (B1 = la première case de la ligne du bas, B2 = la deuxième case de la ligne du bas)
btn_B1 = customtkinter.CTkButton(root, text="", bg_color='#323232', fg_color='#323232', hover_color='white', width=50, height=50, command=print_pawns_B1)
btn_B1.place(x=115, y=185)
all_cases.append(btn_B1)
btn_B2 = customtkinter.CTkButton(root, text="", bg_color='#323232', fg_color='#323232', hover_color='white', width=50, height=50, command=print_pawns_B2)
btn_B2.place(x=170, y=185)
all_cases.append(btn_B2)
btn_B3 = customtkinter.CTkButton(root, text="", bg_color='#323232', fg_color='#323232', hover_color='white', width=50, height=50, command=print_pawns_B3)
btn_B3.place(x=225, y=185)
all_cases.append(btn_B3)

# Création d'une case qui permet de faire passer des informations au joueurs
informations = customtkinter.CTkEntry(root, placeholder_text='Les informations sur le jeux apparaiterons ici', placeholder_text_color='grey', bg_color="white", fg_color='white', text_color="black", width=270, justify='center')
informations.place(x=65, y=250)

# Création du bouton pour lancer la partie
btn_start = customtkinter.CTkButton(root, text="Jouer", font=("Arial",16), bg_color='white', fg_color='green', text_color='white', width=70, height=50, command=start)
btn_start.place(x=160, y=300)

root.mainloop()