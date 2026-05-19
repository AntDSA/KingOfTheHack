import pygame as p
import game as g
import random
from setting import Setting


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

        w, h = screen.get_width(), screen.get_height()
        panel_w = w - 400
        self.rect_panel = p.Rect(0, 0, panel_w, h)
        self.rect_titre = p.Rect(MARGE, MARGE, panel_w - 2*MARGE, 30)

    def handle_event(self, event, game):
        pass

        if event.type == p.MOUSEWHEEL:
            if self.rect_panel.collidepoint(p.mouse.get_pos()):
                self.scroll_offset = max(0, self.scroll_offset - event.y * LIGNE_H)

    def update(self):
        pass

    def draw(self):
        p.draw.rect(self.screen, (15, 15, 15), self.rect_panel)
        p.draw.rect(self.screen, self.GREEN, self.rect_panel, 1)

        # Titre
        self.screen.blit(
            self.font.render("[ Essai de Phishing / Erreur de scroll ]", True, self.GREEN),
            (self.rect_titre.x, self.rect_titre.y)
        )