import pygame as p
import game as g
import random
from setting import Setting
from data.missions import MAILS


LIGNE_H  = 64
MARGE    = 10
HEADER_H = 70

class Phishing():
    def __init__(self, screen, font, colors, game):
        self.screen = screen
        self.font   = font
        self.GREEN  = colors["GREEN"]
        self.BG     = colors["BG"]
        self.game   = game

        self.w, self.h = screen.get_width(), screen.get_height()
        panel_w = self.w - 400
        self.rect_panel = p.Rect(0, 0, panel_w, self.h)
        self.rect_panel2 = p.Rect(0, HEADER_H, panel_w, self.h - HEADER_H)
        self.rect_titre = p.Rect(MARGE, MARGE, panel_w - 2*MARGE, 30)


    def _items(self):
        pass

    def _rect_item(self, index):
        pass
    def _cliquer(self, nom):
        pass
    def handle_event(self, event, game):
        pass
    def update(self):
        pass

    def draw(self):
        p.draw.rect(self.screen, (15, 15, 15), self.rect_panel)
        p.draw.rect(self.screen, self.GREEN, self.rect_panel, 1)
        p.draw.rect(self.screen, self.GREEN, self.rect_panel2, 1)

        # Mail
        
        # Contenue du mail
    
        # Titre
        self.screen.blit(
            self.font.render("[ Essai de Phishing / Erreur de scroll ]", True, self.GREEN),
            (self.rect_titre.x, self.rect_titre.y)
        )