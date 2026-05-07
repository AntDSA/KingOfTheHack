import pygame as p
import sys

class Bureau():
    def __init__(self, screen, font, colors):
        self.screen = screen
        self.font = font
        self.BG = colors["BG"]
        self.GREEN = colors["GREEN"]

        # Icônes cliquables — liste de (label, rect, état_cible)
        self.icones = [
            {"label": "[Mes fichiers]", "rect": p.Rect(50, 100, 200, 40), "cible": "labyrinthe"},
            {"label": "[Boite mail]",   "rect": p.Rect(50, 160, 200, 40), "cible": "phishing"},
            {"label": "[Terminal]",     "rect": p.Rect(50, 220, 200, 40), "cible": "cesar"},
        {"label": "[Quitter]", "rect": p.Rect(20, self.screen.get_height() - 50, 150, 35), "cible": "quitter"},
        ]

                    
    def handle_event(self, event, game):
        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            for icone in self.icones:
                if icone["rect"].collidepoint(event.pos):
                    if icone["cible"] == "quitter":
                        p.quit()
                        sys.exit()
                    else:
                        game.set_state(icone["cible"])
        

    def update(self):
        pass

    def draw(self):
        # Icônes
        for icone in self.icones:
            # Bordure si survol
            souris = p.mouse.get_pos()
            if icone["rect"].collidepoint(souris):
                p.draw.rect(self.screen, self.GREEN, icone["rect"], 1)

            texte = self.font.render(icone["label"], True, self.GREEN)
            self.screen.blit(texte, (icone["rect"].x + 5, icone["rect"].y + 10))
