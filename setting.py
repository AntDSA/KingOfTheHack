import pygame as p
# encore test github
class Setting:
    def __init__(self, screen):
        self.screen = screen
        self.width = 1200
        self.height = 800
        self.volume = 0.5
        self.dark_mode = True
        self.font = p.font.SysFont("consolas", 30)
        self.bg_color = (0, 0, 0)
        self.text_color = (0, 255, 0)

    def draw(self):
        if self.dark_mode:
            self.bg_color = (0, 0, 0)
            self.text_color = (0, 255, 0)
        else:
            self.bg_color = (255, 255, 255)
            self.text_color = (0, 0, 0)

        self.screen.fill(self.bg_color)

        # changement : liste pour éviter les répétitions de blit
        textes = [
            ("SETTINGS",                          (500, 100)),
            (f"Volume : {int(self.volume*100)}%", (400, 250)),
            (f"Mode : {'Dark' if self.dark_mode else 'Light'}", (400, 320)),
            (f"Resolution : {self.width}x{self.height}", (400, 390)),
            ("Press ESC to return",               (400, 500)),
        ]
        for label, pos in textes:
            self.screen.blit(self.font.render(label, True, self.text_color), pos)

    def handle_event(self, event):
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                self.volume = min(1.0, self.volume + 0.1)
                p.mixer.music.set_volume(self.volume)
            if event.key == p.K_DOWN:
                self.volume = max(0.0, self.volume - 0.1)
                p.mixer.music.set_volume(self.volume)
            if event.key == p.K_m:
                self.dark_mode = not self.dark_mode
            if event.key == p.K_r:
                if self.width == 1200:
                    self.width, self.height = 800, 600
                else:
                    self.width, self.height = 1200, 800
                self.screen = p.display.set_mode((self.width, self.height))
