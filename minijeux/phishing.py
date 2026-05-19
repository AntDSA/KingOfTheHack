import pygame as p
import game as g
import random
from setting import Setting
class phishing():
    def __init__(self, screen, font, colors, arbre, game):
        self.screen = screen
        self.font   = font
        self.GREEN  = colors["GREEN"]
        self.BG     = colors["BG"]
        self.game   = game


    def draw(self):
        self