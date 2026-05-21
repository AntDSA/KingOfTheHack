import pygame as p
import sys
import setting
from interface.bureau import Bureau
from interface.blocnote import Blocnote
from minijeux.labyrinthe import Labyrinthe
from minijeux.phishing import Phishing
from data.filesystems import LABYRINTHE_1, LABYRINTHE_2, LABYRINTHE_3

class Game():
    def __init__(self):
        p.init()
        info = p.display.Info()
        self.width  = min(1200, info.current_w - 20)
        self.height = min(800,  info.current_h - 80)
        self.screen = p.display.set_mode((self.width, self.height))
        p.display.set_caption("King of the Hack")
        self.clock   = p.time.Clock()
        self.running = True

        self.state = "bureau"
        # changement : state_precedent initialisé pour éviter AttributeError au démarrage. J'ai déjà eu ce problème avec une modif
        self.state_precedent = "bureau"

        self.BG    = (13, 13, 13)
        self.GREEN = (0, 255, 65)

        self.font = p.font.SysFont("consolas", 20)

        colors = {"BG": self.BG, "GREEN": self.GREEN}
        self.bureau   = Bureau(self.screen, self.font, colors)
        self.blocnote = Blocnote(self.screen, self.font, colors)
        self.blocnote.set_mission("Ton PC a été infecté. Suis les instructions.", timer_secondes=120)

        self.setting = setting.Setting(self.screen)
        self.labyrinthe = None  # sera créé au lancement d'une mission
        self.phishing = None  # sera créé au lancement d'une mission
        self.mission_points = 0

    def set_state(self, nouvel_etat):
        self.state_precedent = self.state
        self.state = nouvel_etat

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                self.handle_event(event)
            self.update(dt)
            self.draw()
            p.display.flip()

    def handle_event(self, event):
        # changement : blocnote.handle_event appelé une seule fois (était appelé deux fois dans "bureau")
        action = self.blocnote.handle_event(event)
        if action == "home":
            self.set_state("bureau")
        elif action == "retour":
            self.set_state(self.state_precedent)

        if self.state == "bureau":
            self.bureau.handle_event(event, self)
        elif self.state == "labyrinthe":
            self.labyrinthe.handle_event(event, self)
        elif self.state == "phishing":
            self.phishing.handle_event(event, self)
            
        elif self.state == "cesar":
            pass
        elif self.state == "sql":
            pass
        elif self.state == "fin":
            pass

    def update(self, dt):
        self.blocnote.update(dt)
        if self.state == "labyrinthe":
            self.labyrinthe.update()
        elif self.state == "phishing":
            self.phishing.update()

    def draw(self):
        self.screen.fill(self.BG)

        # changement : dictionnaire pour éviter la répétition des elif + texte simple
        ecrans_simples = {
            "phishing": "PHISHING",
            "cesar":    "CESAR",
            "sql":      "SQL",
            "fin":      "FIN — le virus a disparu",
        }

        if self.state == "bureau":
            self.bureau.draw()
        elif self.state == "labyrinthe":
            self.labyrinthe.draw()
        elif self.state == "phishing":
            self.phishing.draw()
        elif self.state in ecrans_simples:
            self.screen.blit(
                self.font.render(ecrans_simples[self.state], True, self.GREEN),
                (20, 20)
            )

        self.blocnote.draw()

    def lancer_labyrinthe(self, arbre, points, texte):
        from minijeux.labyrinthe import Labyrinthe
        self.labyrinthe = Labyrinthe(
            self.screen, self.font,
            {"BG": self.BG, "GREEN": self.GREEN},
            arbre, self
        )

        self.mission_points = points
        self.blocnote.set_mission(texte, timer_secondes=120)
        self.set_state("labyrinthe")

    def lancer_phishing(self, points, texte):
        self.phishing = Phishing(
            self.screen, self.font,
            {"BG": self.BG, "GREEN": self.GREEN},
            self
        )

        self.mission_points = points
        self.blocnote.set_mission(texte, timer_secondes=120)
        self.set_state("phishing")
    def lancer_phishing(self, points, texte):
        self.phishing = Phishing(
            self.screen, self.font,
            {"BG": self.BG, "GREEN": self.GREEN},
            None
        )

        self.mission_points = points
        self.blocnote.set_mission(texte, timer_secondes=120)
        self.set_state("phishing")