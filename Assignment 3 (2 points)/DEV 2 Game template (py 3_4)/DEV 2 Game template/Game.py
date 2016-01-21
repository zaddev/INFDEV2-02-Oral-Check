﻿import time
from threading import Thread
import os, pygame
import time
from Tile import *
from Node import *
from Boat import *
pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 50
size = 10
entry_roads, entry_rivers, bridges = build_scene(size, offset)

#faces to the right
boat_texture = pygame.image.load("Content/tanker.png").convert_alpha()

#faces to the right
car_texture = pygame.image.load("Content/car.png").convert_alpha()



def Update(entities):
  #TODO INSERT MISSING LINE BELOW
  return newEntities


def Draw(entities):
  #TODO INSERT MISSING LINE BELOW

def Main():
  start = time.time()
  entities = Node(Boat(entry_rivers.Value, boat_texture), Node(Car(entry_roads.Value, car_texture), Empty))
  while True:    
    pygame.event.pump()
    screen.fill(green)

    #here we draw the board, do not move
    _board = entry_roads
    while not _board.IsEmpty:
      _board.Value.Draw(screen, False)
      _board = _board.Tail

    #here we draw the bridges, do not move
    _board = bridges
    while not _board.IsEmpty:
      _board.Value.Draw(screen, True)
      _board = _board.Tail

    entities = Update(entities)
    Draw(entities) 

    if random.randint(0,100) < 5:
      entities = Node(Boat(entry_rivers.Value, boat_texture), Node(Car(entry_roads.Value, car_texture), entities))


    pygame.display.flip()
    time.sleep(0.2)
    
Main()
