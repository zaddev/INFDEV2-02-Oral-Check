﻿import random
class Node:
  def __init__(self, value, tail):
    self.Tail = tail
    self.Value = value
    self.IsEmpty = False
  def Iter(self,f):
    f(self.Value)
    self.Tail.Iter(f)
  def Map(self,f):
    #TODO INSERT MISSING LINE BELOW
  def Filter(self,p):
    #TODO INSERT MISSING LINE BELOW
      return Node(self.Value, self.Tail.Filter(p))
    else:
      return self.Tail.Filter(p)

class Empty: 
  def __init__(self):
    self.IsEmpty = True
  def Iter(self,f):
    return
  def Map(self,f):
    return Empty
  def Filter(self,p):
    return Empty

Empty = Empty()

def AUX_length(l, acc):
  if l.IsEmpty: return acc
  else: return AUX_length(l.Tail, acc + 1)

def length(l):
  return AUX_length(l, 0)

def select_one_random(l):
  _length = length(l)
  rnd_num = int(random.uniform(0, _length ))
  while(rnd_num > 0):
    l = l.Tail
    rnd_num -= 1
  return l.Value
  

