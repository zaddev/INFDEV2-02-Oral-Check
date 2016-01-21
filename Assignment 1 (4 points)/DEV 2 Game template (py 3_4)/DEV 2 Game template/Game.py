﻿import time
from threading import Thread
import os, pygame
import time
from Tile import *
from Node import *

pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 30
board_size = 10
car_texture = pygame.image.load("Content/car.png").convert()
entry_tile = build_square_matrix(board_size, offset)


def Update(cars):
  newCars = Empty
  #TODO INSERT MISSING LINE BELOW!
    car = cars.Value
    if car.Tile.Right is not None and car.Tile.Right.Traverseable:
      newCar = Car(car.Tile.Right)
    else:
      newCar = car
    newCars = Node(newCar, newCars)
    #TODO INSERT MISSING LINE BELOW!
  return newCars


def Draw(cars):
  while cars.IsEmpty is False:
    #TODO INSERT MISSING LINE BELOW!
    _width = int(offset / 3)
    screen.blit(pygame.transform.scale(car_texture, (_width, _width)), 
                     (_width + car.Tile.Position.X * offset, 
                      _width + car.Tile.Position.Y * offset))
    cars = cars.Tail


def Main():
  start = time.time()
  cars = Node(Car(entry_tile), Empty)
  while True:
    pygame.event.pump()    
    screen.fill(green)  
    entry_tile.Reset()
    entry_tile.Draw(screen)

    cars = Update(cars)
    Draw(cars)

    pygame.display.flip()
    time.sleep(1)
    
Main()
