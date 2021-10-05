import pgzrun
import time
import random

currentimage = 1
currentfoto = 1
WIDTH = 446
HEIGHT = 540

garrafa = 250


lista = []







scorpion = Actor("scorpion_1",(223,random.randint(0, 540)))
lista.append(scorpion)
scorpion = Actor("scorpion_1",(223,random.randint(0, 540)))
lista.append(scorpion)

scorpion = Actor("scorpion_1",(223,random.randint(0, 540)))
lista.append(scorpion)

scorpion = Actor("scorpion_1",(223,random.randint(0, 540)))
lista.append(scorpion)

scorpion = Actor("scorpion_1",(223,random.randint(0, 540)))
lista.append(scorpion)
dino = Actor("dino")

def draw ():
    screen.clear()
    screen.fill((0, 187, 255))
    dino.draw()
    for s in lista:
        s.draw()

start = True
def update():
    global garrafa
    dino.pos = 100,garrafa
    global start
    if start == True:
        clock.schedule_interval(animatedino,0.2)
        clock.schedule_interval(animatescorpion,0.2)
        start = False
    if keyboard.w == True:
        garrafa = garrafa - 10
    if keyboard.s == True:
        garrafa = garrafa + 10
    if garrafa == 550:
        garrafa = 540
    if garrafa == -10:
        garrafa = 0
    if dino.colliderect(scorpion) == True:
        dino.image = "dino1"
def animatedino():
    global currentimage
    dino.image = "dino" + str(currentimage)
    currentimage = currentimage %2+3
def animatescorpion():
    global currentfoto
    for s in lista:
        s.image = "scorpion_" + str(currentfoto)
    currentfoto = currentfoto %7+1
 




pgzrun.go()