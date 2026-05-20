# p.draw.rect => tracer un rectangle 
#blit => position
#if event.type == p.Keydown: 
#     if event.type == something
#p.mouse.get_pos()
# => click de la souris (voir bureau.py) 
#créer un nouveau fichier et le relier à game  
#Mission : Faire une page de paramètre qui interagit avec setting 

# fichier : parametre_page.py

import pygame as p
from parametre import Setting

class ParametrePage:

    def __init__(self, screen):

        self.screen = screen

        # récupération de la classe Setting
        self.setting = Setting(screen)

        self.font = p.font.SysFont("consolas", 30)

        # ===== BOUTONS =====

        # volume +
        self.btn_plus = p.Rect(750, 250, 50, 50)

        # volume -
        self.btn_minus = p.Rect(300, 250, 50, 50)

        # mode sombre
        self.btn_mode = p.Rect(300, 350, 500, 60)

        # résolution
        self.btn_resolution = p.Rect(300, 450, 500, 60)

    # =========================================

    def draw(self):

        # couleurs selon le mode
        if self.setting.dark_mode:

            bg_color = (0, 0, 0)
            text_color = (0, 255, 0)
            button_color = (40, 40, 40)

        else:

            bg_color = (255, 255, 255)
            text_color = (0, 0, 0)
            button_color = (180, 180, 180)

        self.screen.fill(bg_color)

        # ===== TITRE =====

        titre = self.font.render("PARAMETRES", True, text_color)
        self.screen.blit(titre, (450, 100))

        # =========================================
        # VOLUME
        # =========================================

        texte_volume = self.font.render(
            f"Volume : {int(self.setting.volume * 100)}%",
            True,
            text_color
        )

        self.screen.blit(texte_volume, (430, 260))

        # bouton -
        p.draw.rect(self.screen, button_color, self.btn_minus)

        moins = self.font.render("-", True, text_color)
        self.screen.blit(moins, (318, 255))

        # bouton +
        p.draw.rect(self.screen, button_color, self.btn_plus)

        plus = self.font.render("+", True, text_color)
        self.screen.blit(plus, (765, 255))

        # =========================================
        # MODE SOMBRE
        # =========================================

        p.draw.rect(self.screen, button_color, self.btn_mode)

        texte_mode = self.font.render(
            f"Mode : {'Dark' if self.setting.dark_mode else 'Light'}",
            True,
            text_color
        )

        self.screen.blit(texte_mode, (380, 365))

        # =========================================
        # RESOLUTION
        # =========================================

        p.draw.rect(self.screen, button_color, self.btn_resolution)

        texte_resolution = self.font.render(
            f"Resolution : {self.setting.width}x{self.setting.height}",
            True,
            text_color
        )

        self.screen.blit(texte_resolution, (340, 465))

        # =========================================
        # RETOUR
        # =========================================

        retour = self.font.render(
            "Appuie sur ESC pour revenir",
            True,
            text_color
        )

        self.screen.blit(retour, (330, 650))

    # =========================================

    def handle_event(self, event):

        # clavier
        if event.type == p.KEYDOWN:

            if event.key == p.K_ESCAPE:
                return "menu"

        # souris
        if event.type == p.MOUSEBUTTONDOWN:

            mouse_pos = p.mouse.get_pos()

            # ==========================
            # BOUTON VOLUME +
            # ==========================

            if self.btn_plus.collidepoint(mouse_pos):

                self.setting.volume = min(
                    1.0,
                    self.setting.volume + 0.1
                )

                p.mixer.music.set_volume(
                    self.setting.volume
                )

            # ==========================
            # BOUTON VOLUME -
            # ==========================

            if self.btn_minus.collidepoint(mouse_pos):

                self.setting.volume = max(
                    0.0,
                    self.setting.volume - 0.1
                )

                p.mixer.music.set_volume(
                    self.setting.volume
                )

            # ==========================
            # BOUTON MODE
            # ==========================

            if self.btn_mode.collidepoint(mouse_pos):

                self.setting.dark_mode = not self.setting.dark_mode

            # ==========================
            # BOUTON RESOLUTION
            # ==========================

            if self.btn_resolution.collidepoint(mouse_pos):

                if self.setting.width == 1200:

                    self.setting.width = 800
                    self.setting.height = 600

                else:

                    self.setting.width = 1200
                    self.setting.height = 800

                self.screen = p.display.set_mode(
                    (
                        self.setting.width,
                        self.setting.height
                    )
                )

