import pygame as p
# INES
# Paramètre des images du menu (blanc ou noir)
# Paramètre taille de l'écran qui modifie les pixels (on va donc faire des calculs de math selon moi pour adapter nos images)
# Paramètre du son et du choix des musiques

class Setting:
    def __init__(self, screen):
        self.screen = screen

        # Taille écran
        self.width = 1200
        self.height = 800

        # Paramètres
        self.volume = 0.5
        self.dark_mode = True

        # Police
        self.font = p.font.SysFont("consolas", 30)

        # Couleurs (style hacking)
        self.bg_color = (0, 0, 0)
        self.text_color = (0, 255, 0)

    def draw(self):
        # Fond
        if self.dark_mode:
            self.bg_color = (0, 0, 0)
            self.text_color = (0, 255, 0)
        else:
            self.bg_color = (255, 255, 255)
            self.text_color = (0, 0, 0)

        self.screen.fill(self.bg_color)

        # Textes
        title = self.font.render("SETTINGS", True, self.text_color)
        volume = self.font.render(f"Volume : {int(self.volume * 100)}%", True, self.text_color)
        mode = self.font.render(f"Mode : {'Dark' if self.dark_mode else 'Light'}", True, self.text_color)
        resolution = self.font.render(f"Resolution : {self.width}x{self.height}", True, self.text_color)
        back = self.font.render("Press ESC to return", True, self.text_color)

        # Positions
        self.screen.blit(title, (500, 100))
        self.screen.blit(volume, (400, 250))
        self.screen.blit(mode, (400, 320))
        self.screen.blit(resolution, (400, 390))
        self.screen.blit(back, (400, 500))

    def handle_event(self, event):
        if event.type == p.KEYDOWN:

            # Volume
            if event.key == p.K_UP:
                self.volume = min(1.0, self.volume + 0.1)
                p.mixer.music.set_volume(self.volume)

            if event.key == p.K_DOWN:
                self.volume = max(0.0, self.volume - 0.1)
                p.mixer.music.set_volume(self.volume)

            # Mode sombre / clair
            if event.key == p.K_m:
                self.dark_mode = not self.dark_mode

            # Changer résolution
            if event.key == p.K_r:
                if self.width == 1200:
                    self.width, self.height = 800, 600
                else:
                    self.width, self.height = 1200, 800

                self.screen = p.display.set_mode((self.width, self.height))
    # def screenModification(self):
        
