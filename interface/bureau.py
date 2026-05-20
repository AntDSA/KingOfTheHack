import pygame as p
import sys

# Réécriture du code au propre (seulement espace et tab)
# pas de changement de logique ou de structure

class Bureau():

    def __init__(self, screen, font, colors):

        self.screen = screen
        self.font = font

        self.BG = colors["BG"]
        self.GREEN = colors["GREEN"]

        self.icones = [

            {
                "label": "[Mes fichiers]",
                "rect": p.Rect(50, 100, 200, 40),
                "cible": "labyrinthe"
            },

            {
                "label": "[Boite mail]",
                "rect": p.Rect(50, 160, 200, 40),
                "cible": "phishing"
            },

            {
                "label": "[Terminal]",
                "rect": p.Rect(50, 220, 200, 40),
                "cible": "cesar"
            },

            # =========================
            # NOUVEAU BOUTON PARAMETRE
            # =========================

            {
                "label": "[Parametres]",
                "rect": p.Rect(50, 280, 200, 40),
                "cible": "parametre"
            },

            {
                "label": "[Quitter]",
                "rect": p.Rect(
                    20,
                    self.screen.get_height() - 50,
                    150,
                    35
                ),
                "cible": "quitter"
            },

        ]

    # =========================================

    def handle_event(self, event, game):

        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:

            for icone in self.icones:

                if icone["rect"].collidepoint(event.pos):

                    # =========================
                    # QUITTER
                    # =========================

                    if icone["cible"] == "quitter":

                        p.quit()
                        sys.exit()

                    # =========================
                    # LABYRINTHE
                    # =========================

                    elif icone["cible"] == "labyrinthe":

                        from data.filesystems import SELECTION_FICHIERS

                        game.lancer_labyrinthe(

                            SELECTION_FICHIERS,
                            8,

                            "Ouvre le bon dossier pour commencer ta mission."

                        )

                    # =========================
                    # PARAMETRES
                    # =========================

                    elif icone["cible"] == "parametre":

                        game.set_state("parametre")

    # =========================================

    def update(self):

        pass

    # =========================================

    def draw(self):

        souris = p.mouse.get_pos()

        for icone in self.icones:

            # contour quand souris dessus
            if icone["rect"].collidepoint(souris):

                p.draw.rect(
                    self.screen,
                    self.GREEN,
                    icone["rect"],
                    1
                )

            # texte
            self.screen.blit(

                self.font.render(
                    icone["label"],
                    True,
                    self.GREEN
                ),

                (
                    icone["rect"].x + 5,
                    icone["rect"].y + 10
                )

            )
