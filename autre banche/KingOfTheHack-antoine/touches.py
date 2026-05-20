import pygame as p

p.init()
p.mixer.init()

class Settings:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.screen = p.display.set_mode((self.width, self.height))
        p.display.set_caption("Settings Menu")

        self.clock = p.time.Clock()

        self.volume = 0.5
        self.dark_mode = True

        self.font = p.font.SysFont("consolas", 30)

        self.bg_color = (0, 0, 0)
        self.text_color = (0, 255, 0)

        self.controls = {
            "UP": p.K_z,
            "DOWN": p.K_s,
            "LEFT": p.K_q,
            "RIGHT": p.K_d,
            "ACTION": p.K_SPACE
        }

        self.waiting_for_key = None
        self.selected_action = 0
        self.actions_list = list(self.controls.keys())

    def draw(self):
        if self.dark_mode:
            self.bg_color = (0, 0, 0)
            self.text_color = (0, 255, 0)
        else:
            self.bg_color = (255, 255, 255)
            self.text_color = (0, 0, 0)

        self.screen.fill(self.bg_color)

        title = self.font.render("SETTINGS", True, self.text_color)
        volume = self.font.render(f"Volume : {int(self.volume * 100)}%", True, self.text_color)
        mode = self.font.render(f"Mode : {'Dark' if self.dark_mode else 'Light'}", True, self.text_color)
        resolution = self.font.render(f"Resolution : {self.width}x{self.height}", True, self.text_color)

        self.screen.blit(title, (500, 50))
        self.screen.blit(volume, (400, 150))
        self.screen.blit(mode, (400, 200))
        self.screen.blit(resolution, (400, 250))

        controls_title = self.font.render("Controls :", True, self.text_color)
        self.screen.blit(controls_title, (400, 320))

        y_offset = 370
        for i, action in enumerate(self.actions_list):
            key = self.controls[action]
            key_name = p.key.name(key)

            prefix = "-> " if i == self.selected_action else "   "

            text = self.font.render(f"{prefix}{action} : {key_name}", True, self.text_color)
            self.screen.blit(text, (400, y_offset))
            y_offset += 40

        # Message changement touche
        if self.waiting_for_key:
            msg = self.font.render("Press a key...", True, (255, 0, 0))
            self.screen.blit(msg, (400, y_offset + 20))
        else:
            msg = self.font.render("ENTER to change key", True, self.text_color)
            self.screen.blit(msg, (400, y_offset + 20))

        back = self.font.render("ESC to quit", True, self.text_color)
        self.screen.blit(back, (400, y_offset + 60))

    def handle_event(self, event):
        if event.type == p.KEYDOWN:

            # Modif touche
            if self.waiting_for_key:
                action = self.actions_list[self.selected_action]
                self.controls[action] = event.key
                self.waiting_for_key = None
                return

            if event.key == p.K_UP:
                self.selected_action = (self.selected_action - 1) % len(self.actions_list)

            elif event.key == p.K_DOWN:
                self.selected_action = (self.selected_action + 1) % len(self.actions_list)

            elif event.key == p.K_RETURN:
                self.waiting_for_key = True

            elif event.key == p.K_RIGHT:
                self.volume = min(1.0, self.volume + 0.1)
                p.mixer.music.set_volume(self.volume)

            elif event.key == p.K_LEFT:
                self.volume = max(0.0, self.volume - 0.1)
                p.mixer.music.set_volume(self.volume)

            elif event.key == p.K_m:
                self.dark_mode = not self.dark_mode

            elif event.key == p.K_r:
                if self.width == 1200:
                    self.width, self.height = 800, 600
                else:
                    self.width, self.height = 1200, 800

                self.screen = p.display.set_mode((self.width, self.height))

    def run(self):
        running = True

        player = p.Rect(600, 400, 50, 50)

        while running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False

                if event.type == p.KEYDOWN and event.key == p.K_ESCAPE:
                    running = False

                self.handle_event(event)

            keys = p.key.get_pressed()

            if not self.waiting_for_key:
                if keys[self.controls["UP"]]:
                    player.y -= 5
                if keys[self.controls["DOWN"]]:
                    player.y += 5
                if keys[self.controls["LEFT"]]:
                    player.x -= 5
                if keys[self.controls["RIGHT"]]:
                    player.x += 5
                    
            self.draw()

            # Dessin joueur
            p.draw.rect(self.screen, (255, 0, 0), player)

            p.display.flip()
            self.clock.tick(60)

        p.quit()



if __name__ == "__main__":
    Settings().run()
