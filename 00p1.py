# -*- coding: utf-8 -*-
"""00P1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XCx0v7yTySnSF_pOVyw5n4STtVlcyFE5
"""

import random
class human:
  def __init__(self,name) :
    self.name = name

class footballer(human):
  def __init__(self,name):
    super().__init__(name)

def assign_players(players):
  random.shuffle(players)
  teamA=players[:11]
  teamB=players[11:]
  return teamA,teamB

players_name =["حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار", "میلاد",
                  "مصطفی", "امین", "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل",
                  "بهروز", "شهروز", "سامان", "محسن"]
players=[footballer(name)for name in players_name]
teamA,teamB = assign_players(players)

for players in teamA:
  print (f"{players.name} is team A")
for players in teamB:
  print(f"{players.name} is team B")