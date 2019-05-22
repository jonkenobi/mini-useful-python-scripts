# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:21:30 2019

@author: jonathan
"""

class Pokemon:
    def __init__(self,name):
      self.lvl = 1
      self.name = name
    def get_level():
        print(name +"is level"+lvl)
class Charizard(Pokemon):
    def __init__(self):
        self.name = "Charizard"
        self.moves = {"Flamethrower":120}
    
class Mewtwo(Pokemon):
    def __init__(self):
        self.moves = {"Psychic Beam":110}
        self.name = "Mewtwo"
def fight(Pokemon1,Pokemon2):
    Move1 = list(Pokemon1.moves.keys())[0]
    Move2 = list(Pokemon2.moves.keys())[0]
    print(Pokemon1.name+" used "+list(Pokemon1.moves.keys())[0])
    print(Pokemon2.name+" used "+list(Pokemon2.moves.keys())[0])
    result = Pokemon1.moves[Move1]-Pokemon2.moves[Move2]
    if result>0:
        print(Pokemon1.name+" wins")
    else:
        print(Pokemon2.name+ " wins")
        
Hilmi= Charizard()
Prince = Mewtwo()
fight(Prince,Hilmi)