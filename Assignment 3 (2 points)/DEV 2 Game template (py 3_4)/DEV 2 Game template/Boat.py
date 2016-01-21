﻿﻿import pygame
import random
from Node import *
from Common import *

class Boat:
  def __init__(self, tile, texture):
    self.Tile = tile
    self.Texture = texture


  #TODO INSERT MISSING LINE BELOW
    r = random.randint(0,4)
    if r == 0 and self.Tile.Right is not None and (self.Tile.Right.River or self.Tile.Right.Harbor):
      return Boat(self.Tile.Right, self.Texture)
    elif r == 1 and self.Tile.Left is not None and (self.Tile.Left.River or self.Tile.Left.Harbor):
      return Boat(self.Tile.Left, self.Texture)
    elif r == 2 and self.Tile.Down is not None and (self.Tile.Down.River or self.Tile.Down.Harbor):
      return Boat(self.Tile.Down, self.Texture)
    elif r == 3 and self.Tile.Up is not None and (self.Tile.Up.River or self.Tile.Up.Harbor):
      return Boat(self.Tile.Up, self.Texture)
    else:
      return self


  #TODO INSERT MISSING LINE BELOW
    return self.Tile.Harbor

  def Draw(self, screen, offset):
    _width = int(offset / 3)
    screen.blit(pygame.transform.scale(self.Texture, (_width, _width)), 
                     (_width + self.Tile.Position.X * offset, 
                      _width + self.Tile.Position.Y * offset))
