import pygame as p

# caractéristique de notre personnage
# il n'aura que les PV et un blockNote qui résume ce qu'il possède comme indice

class player():
    def __init__(self):
        self.health = 50
        self.something = None