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


    def _items(self):
        return list(self.position_actuelle.keys())

    def _rect_item(self, index):
        y = self.rect_liste.y + index * LIGNE_H - self.scroll_offset
        return p.Rect(self.rect_liste.x, y, self.rect_liste.width, LIGNE_H - 3)

    def _cliquer(self, nom):
        valeur = self.position_actuelle[nom]

    def handle_event(self, event, game):
        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            items = self._items()
            for i, nom in enumerate(items):
                rect = self._rect_item(i)
                if rect.collidepoint(event.pos) and self.rect_liste.collidepoint(event.pos):
                    self._cliquer(nom)
                    return

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