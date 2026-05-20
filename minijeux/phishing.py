import pygame as p
import game as g
import random
from setting import Setting


LIGNE_H  = 64
MARGE    = 10
HEADER_H = 70

class phishing():
    def __init__(self, screen, font, colors, mails, game):
        self.screen = screen
        self.font   = font
        self.GREEN  = colors["GREEN"]
        self.BG     = colors["BG"]
        self.game   = game
        self.mails  = mails
        w, h = screen.get_width(), screen.get_height()
        panel_w = w - 400
        self.rect_panel = p.Rect(0, 0, panel_w, h)
        self.rect_panel2 = p.Rect(0, 50, panel_w, h)
        self.rect_titre = p.Rect(MARGE, MARGE, panel_w - 2*MARGE, 30)
        self.scroll_offset = 0
    
    
    def _items(self):
        pass
    def _rect_item(self, index):
        pass
    def _cliquer(self, nom):
        pass
    def update(self):
        pass
    def handle_event(self, event):
        pass
    def draw(self):
        p.draw.rect(self.screen, (15, 15, 15), self.rect_panel)
        p.draw.rect(self.screen, self.GREEN, self.rect_panel, 1)
        
        p.draw.rect(self.screen, self.GREEN, self.rect_panel2, 1)

        # Titre
        self.screen.blit(
            self.font.render("[ PHISHING ]", True, self.GREEN),
            (self.rect_titre.x, self.rect_titre.y)
        )
