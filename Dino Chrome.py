import pgzrun
import time
import random

currentimage = 1
currentfoto = 1
currentmolhado = 1
WIDTH = 446
HEIGHT = 540

garrafa = 250
aguaX = 100
aguas = []


lista = [Actor("scorpion_1",(223,random.randint(0, 540)))]




def spawn():
    if len(lista) <= 8:
        scorpion = Actor("scorpion_1",(223,random.randint(0, 540)))
        lista.append(scorpion)

        
dino = Actor("dino")


def draw ():
    screen.clear()
    screen.fill((0, 187, 255))
    dino.draw()

    for a in aguas:
        a.draw()
    for s in lista:
        s.draw()

start = True
def update():
    global garrafa, aguaX
    dino.pos = 100,garrafa
    aguaX = aguaX + 1

    global start
    if start == True:
        clock.schedule_interval(animatedino,0.2)
        clock.schedule_interval(animatescorpion,0.2)
        clock.schedule_interval(spawn,4.0)
        clock.schedule_interval(animateagua,1.0)
    onda()
    start = False
    if keyboard.w == True:
        garrafa = garrafa - 10
    if keyboard.s == True:
        garrafa = garrafa + 10
    if garrafa == 550:
        garrafa = 540
    if garrafa == -10:
        garrafa = 0
    if keyboard.space == True:
        agua = Actor("agua1")
        agua.pos = dino.pos
        aguas.append(agua)

    ggwp = len(lista)
    for gg in range (ggwp):
        if dino.colliderect(lista[gg]) == True:
            dino.image = "dino1"
        for a in aguas:
            if a.colliderect(lista[gg]) == True:
                lista.remove(lista[gg])
     
def animatedino():
    global currentimage
    dino.image = "dino" + str(currentimage)
    currentimage = currentimage %2+3
def animatescorpion():
    global currentfoto
    for s in lista:
        s.image = "scorpion_" + str(currentfoto)
    currentfoto = currentfoto %7+1
def animateagua():
    global currentmolhado
    for a in aguas:
        a.image = "agua" + str(currentmolhado)
        currentmolhado = currentmolhado %6+1
def onda():
    for a in aguas:
        a.pos = a.pos[0] + 1, a.pos[1]
    



pgzrun.go()