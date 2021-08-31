import pgzrun
import time



WIDTH = 1550
HEIGHT = 540
















dino = Actor("dino")
def draw ():
    screen.clear()
    screen.fill((0, 187, 255))
    dino.draw()
def update():
    dino.image = "dino6"
    time.sleep(0.3)
    dino.image = "dino5"
    time.sleep(0.3)
    dino.image = "dino4"
    time.sleep(0.3)
    dino.image = "dino3"
    time.sleep(0.3)




pgzrun.go()