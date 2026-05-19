import pygame as p
import sys

# Réécriture du code au propre (seulement espace et tab) pour la lisibilité, pas de changement de logique ou de structure. Aide : IA car la flemme

class Bureau():
    def __init__(self, screen, font, colors):
        self.screen = screen
        self.font = font
        self.BG = colors["BG"]
        self.GREEN = colors["GREEN"]

        self.icones = [
            {"label": "[Mes fichiers]", "rect": p.Rect(50, 100, 200, 40), "cible": "labyrinthe"},
            {"label": "[Boite mail]",   "rect": p.Rect(50, 160, 200, 40), "cible": "phishing"},
            {"label": "[Terminal]",     "rect": p.Rect(50, 220, 200, 40), "cible": "cesar"},
            {"label": "[Quitter]",      "rect": p.Rect(20, self.screen.get_height() - 50, 150, 35), "cible": "quitter"},
        ]

    def handle_event(self, event, game):
        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            for icone in self.icones:
                if icone["rect"].collidepoint(event.pos):
                    if icone["cible"] == "quitter":
                        p.quit()
                        sys.exit()
                    elif icone["cible"] == "labyrinthe":
                        from data.filesystems import LABYRINTHE_1
                        game.lancer_labyrinthe(LABYRINTHE_1, 8, "Infiltre le système. Trouve le bon chemin.")
                    else:
                        game.set_state(icone["cible"])

    def update(self):
        pass

    def draw(self):
        
        souris = p.mouse.get_pos()
        for icone in self.icones:
            if icone["rect"].collidepoint(souris):
                p.draw.rect(self.screen, self.GREEN, icone["rect"], 1)
            
            self.screen.blit(
                self.font.render(icone["label"], True, self.GREEN),
                (icone["rect"].x + 5, icone["rect"].y + 10)
            )