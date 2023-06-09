import numpy as np
import sys
import serial, time
import pygame as pg
import threading, queue
import time
import random

STATO = 0
CONTA = True
TEMPO = 0
TIMER = True

def colpito(listacattivi, pagurorect):
    for cattivone in listacattivi:
        if pagurorect.colliderect(cattivone.get_cattivorect()):
            return True
    return False

class cattivo():
    def __init__(self, y):
        self.cattivoimg = pg.image.load("./pietra.png")
        self.cattivorect = self.cattivoimg.get_rect()
        self.cattivorect.y = y
        self.cattivorect.x = 10

    def muoviti(self):
        self.cattivorect.x += 5

    def mostra(self):
        screen.blit(self.cattivoimg, self.cattivorect)

    def get_x(self):
        return self.cattivorect.x

    def get_y(self):
        return self.cattivorect.y

    def get_cattivorect(self):
        return self.cattivorect


class timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.time = 0
    
    def run(self):
        while CONTA:
            self.time +=1
            time.sleep(1)
    
    def stop(self):
        global CONTA
        CONTA = False
        return self.time   



#pygame config
width = 800
height = 500
sfondo = pg.image.load("./sfondo.jpg")
scritta_start = pg.image.load("./scritta start.png")
scritta_over = pg.image.load("./scritta over.png")
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
paguro = pg.image.load("./paguro.png")
pagurorect = paguro.get_rect()
pagurorect.centerx = width/2
pagurorect.centery = height/2
secondi = timer()

black = 250,235,215
dt = 1
gamma = 0.005
q = queue.Queue()


    


class Read_Microbit(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
      
    def terminate(self):
        self._running = False
        
    def run(self):
        #serial config
        port = "COM5"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            acc = [float(x) for x in data[1:-3].split(",")]
            q.put(acc)
            time.sleep(0.005)


running = True
rm = Read_Microbit()
rm.start()
pg.init()
speed = [0, 0]

listacattivi =[]

def menu():
    screen.blit(sfondo, (0,0))
    screen.blit(scritta_start, (130, height/2-100))
    pg.display.flip()
    clock.tick(20)
    for ev in pg.event.get():
        if((ev.type == pg.KEYDOWN and (ev.key == pg.K_w or ev.key == pg.K_SPACE))):
            print("ciao")
            global STATO
            STATO = 1
        if ev.type == pg.QUIT:
            pg.quit()

def play(pagurorect):
    global TIMER
    spawn = random.randint(0, 10)
    y = random.randint(10, height-10)
    if TIMER:
        secondi.start()
        TIMER = False

    if colpito(listacattivi, pagurorect):
        print("hit")
        global STATO
        global TEMPO
        TEMPO = secondi.stop()
        STATO = 2

    if spawn > 9:
        listacattivi.append(cattivo(y))

    for cattivone in listacattivi:
        cattivone.muoviti()
        if cattivone.get_x() == width:
            listacattivi.pop(0)
                
    screen.blit(sfondo, (0,0))

    acc = q.get()
    speed[0] = (1.-gamma)*speed[0] + dt*acc[0]/120.
    speed[1] = (1.-gamma)*speed[1] + dt*acc[1]/120.
    q.task_done()
    pagurorect = pagurorect.move(speed)
    if pagurorect.left < 0 or pagurorect.right > width:
        speed[0] = -speed[0]
    if pagurorect.top < 0 or pagurorect.bottom > height:
        speed[1] = -speed[1]
        
    screen.blit(paguro, pagurorect)

    for cattivone in listacattivi:
        cattivone.mostra()

    pg.display.flip()
    clock.tick(20)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

def over():
    if listacattivi.__len__() != 0:
        print("pop")
        listacattivi.pop()
    screen.blit(sfondo, (0,0))
    screen.blit(scritta_over, (300, height/2-100))
    pg.display.flip()
    clock.tick(20)
    
    for ev in pg.event.get():
        print(TEMPO)
        if((ev.type == pg.KEYDOWN and (ev.key == pg.K_w or ev.key == pg.K_SPACE))):
            pg.quit()
        if ev.type == pg.QUIT:
            pg.quit()
    
               

def main():

    while STATO == 0:
        menu()

    while STATO == 1:
        play(pagurorect)

    while STATO == 2:
        over()

if __name__ == '__main__':
    main()
        