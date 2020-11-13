from tkinter import *
from PIL import ImageTk,Image
import pygame

root = Tk()
root.title('Pac Man')
root.geometry("800x700")


#Musique
pygame.mixer.init()
pygame.mixer.music.load('pacman_beginning.wav')
pygame.mixer.music.play(loops=-1, start=0.0)



parcours = Canvas(root, width=800, height=690, bg="black")
parcours.pack()

# Dessin parcours
parcours.create_rectangle(0,670,800,690, fill="blue")
parcours.create_rectangle(0,0,800,20, fill="blue")
parcours.create_rectangle(0,230,40,0, fill="blue")
parcours.create_rectangle(0,690,40,350, fill="blue")
parcours.create_rectangle(760,760,800,350, fill="blue")
parcours.create_rectangle(760,220,800,20, fill="blue")
parcours.create_rectangle(80,60,120,100, fill="blue")
parcours.create_rectangle(160,60,280,100, fill="blue")
parcours.create_rectangle(480,60,600,100, fill="blue")
parcours.create_rectangle(640,60,720,100, fill="blue")
parcours.create_rectangle(80,140,120,180, fill="blue")
parcours.create_rectangle(640,140,720,180, fill="blue")
parcours.create_rectangle(160,140,200,300, fill="blue")
parcours.create_rectangle(560,140,600,300, fill="blue")
parcours.create_rectangle(200,215,280,225, fill="gray")
parcours.create_rectangle(480,215,560,225, fill="gray")
parcours.create_rectangle(320,460,440,540, fill="blue")
parcours.create_rectangle(480,500,600,540, fill="blue")
parcours.create_rectangle(160,500,280,540, fill="blue")
parcours.create_rectangle(240,280,340,300, fill="blue")
parcours.create_rectangle(420,280,520,300, fill="blue")
parcours.create_rectangle(240,300,280,380, fill="blue")
parcours.create_rectangle(480,300,520,380, fill="blue")
parcours.create_rectangle(240,360,520,380, fill="blue")
parcours.create_rectangle(240,140,520,160, fill="blue")
parcours.create_rectangle(320,160,440,215, fill="gray")
parcours.create_rectangle(240,420,520,460, fill="blue")
parcours.create_rectangle(160,340,200,460, fill="blue")
parcours.create_rectangle(560,340,600,460, fill="blue")
parcours.create_rectangle(0,220,120,300, fill="blue")
parcours.create_rectangle(640,220,800,300, fill="blue")
parcours.create_rectangle(640,340,800,420, fill="blue")
parcours.create_rectangle(0,340,120,420, fill="blue")
parcours.create_rectangle(320,20,440,100, fill="blue")
parcours.create_rectangle(80,460,120,540, fill="blue")
parcours.create_rectangle(640,460,720,540, fill="blue")
parcours.create_rectangle(80,580,200,620, fill="blue")
parcours.create_rectangle(240,580,520,620, fill="blue")
parcours.create_rectangle(560,580,720,620, fill="blue")

pacman = PhotoImage(file="pacman.png")
phantom_rouge = PhotoImage(file="phantom_rouge.png")
phantom_bleu = PhotoImage(file="phantom_bleu.png")
phantom_rose = PhotoImage(file="phantome_rose.png")
phantom_jaune = PhotoImage(file="phantom_jaune.png")
photo = PhotoImage(file="bonbon.png")


#parcours.create_image(60, 640, image=photo)

def init_balle():
    x = 60
    y = 40
    if y == 40:
        
        while x <= 300:
            parcours.create_image(x, y, image=photo)
            x = x + 40
            if x == 340:
                x = 460
                
        while x <= 740:
            parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 80
        x = 60

    if y == 80:
        while x <= 740:
            if x == 60 or x == 140 or x == 300 or x == 460 or x == 620 or x == 740:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        x = 60
        y = 120
        
    if y == 120:
        while x <= 740:
            parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 160
        x = 60

    if y == 160:
        while x <= 740:
            if x == 60 or x == 140 or x == 220 or x == 540 or x == 620 or x == 740:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 200
        x = 60


    if y == 200:
        while x <= 740:
            if x != 180 and (x < 320 or x > 440) and x != 580:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 240
        x = 60
     

    if y == 240:
        while x <= 740:
            if x == 140 or (x >= 220 and x <= 540) or x == 620:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 280
        x = 60

    if y == 280:
        while x <= 740:
            if x == 140 or x == 220 or x == 540 or x == 620:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 320
        x = 60

    if y == 320:
        while x <= 740:
            if (x < 260 and x > 60) or x >= 540:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 360
        x = 60

    if y == 360:
        while x <= 740:
            if x == 140 or x == 220 or x == 540 or x == 620:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 400
        x = 60

    if y == 400:
        while x <= 740:
            if x == 140 or (x >= 220 and x <= 540) or x == 620:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 440
        x = 60

    if y == 440:
        while x <= 740:
            if x != 180 and (x < 260 or x > 500) and x != 580:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 480
        x = 60

    if y == 480:
        while x <= 740:
            if x != 100 and x != 660 and x != 340 and x != 380 and x != 420 and x != 700 and x != 640:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 520
        x = 60

    if y == 520:
        while x <= 740:
            if x == 60 or x == 140 or x == 300 or x == 460 or x == 620 or x == 740:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 560
        x = 60
            
    if y == 560:
        while x <= 740:
            parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 600
        x = 60

    if y == 600:
        while x <= 740:
            if x == 60 or x == 220 or x == 540 or x == 740:
                parcours.create_image(x, y, image=photo)
            x = x + 40
        y = 640
        x = 60

    if y == 640:
        while x <= 740:
            parcours.create_image(x, y, image=photo)
            x = x + 40

def init_phantom():
    parcours.create_image(300, 320, image=phantom_rouge)
    parcours.create_image(340, 320, image=phantom_bleu)
    parcours.create_image(380, 320, image=phantom_jaune)
    parcours.create_image(420, 320, image=phantom_rose)
    #parcours.create_image(60, 320, image=pacman)


#Une fonction pour le deplacement vers le haut :
def haut(event):
    parcours.move(Pacman,0,-5)

#Une fonction pour le deplacement vers le bas :
def bas(event):
    parcours.move(Pacman,0,5)

#Une fonction pour le deplacement vers la droite :
def droite(event):
    parcours.move(Pacman,5,0)
   
#Une fonction pour le deplacement vers la gauche :
def gauche(event):
    parcours.move(Pacman,-5,0)

Pacman = parcours.create_image(60, 320, image=pacman)
init_phantom()
init_balle()

#On associe les fleches du clavier aux fonctions droite() et gauche():
parcours.bind_all('<Right>', droite)
parcours.bind_all('<Left>', gauche)
parcours.bind_all('<Up>', haut)
parcours.bind_all('<Down>', bas)

mainloop()
