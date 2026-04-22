import pygame as p
import sys

class Game():
    def __init__(self):
        p.init()
        info = p.display.Info()
        self.width = min(1200, info.current_w - 20)
        self.height = min(800, info.current_h - 80) 
        self.screen = p.display.set_mode((self.width, self.height))
        # self.screen = p.display.set_mode((self.width, self.height), p.FULLSCREEN) ## mode fullscreen
        p.display.set_caption("King of the Hack")
        self.clock = p.time.Clock()
        self.running = True

        # États possibles : "bureau", "labyrinthe", "phishing", "cesar", "sql", "fin"
        self.state = "bureau"

        # Couleurs
        self.BG = (13, 13, 13)
        self.GREEN = (0, 255, 65)

        # Police
        self.font = p.font.SysFont("consolas", 20)

        from interface.bureau import Bureau
        self.bureau = Bureau(
            self.screen,
            self.font,
            {"BG": self.BG, "GREEN": self.GREEN}
        )
        from interface.blocnote import Blocnote
        self.blocnote = Blocnote(self.screen, self.font, {"BG": self.BG, "GREEN": self.GREEN})
        self.blocnote.set_mission("Ton PC a été infecté. Suis les instructions.", timer_secondes=120)
        
        
        self.mini_jeu_actif = None

    def set_state(self, nouvel_etat):
        self.state = nouvel_etat

    def run(self):
        while self.running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.running = False
                    p.quit()
                    sys.exit()
                self.handle_event(event)
            self.update()
            self.draw()
            p.display.flip()



    def handle_event(self, event):
        if self.state == "bureau":
            self.bureau.handle_event(event, self)
            self.blocnote.handle_event(event)
            pass  # bureau.handle_event(event) quand bureau.py sera codé
        elif self.state == "labyrinthe":
            pass  # mini_jeu_actif.handle_event(event)
        elif self.state == "phishing":
            pass
        elif self.state == "cesar":
            pass
        elif self.state == "sql":
            pass
        elif self.state == "fin":
            pass


    def update(self):
        if self.state == "bureau":
            dt = self.clock.tick(60) / 1000  # en secondes
            self.blocnote.update(dt)
            pass
        elif self.state == "labyrinthe":
            pass
        elif self.state == "phishing":
            pass
        elif self.state == "cesar":
            pass
        elif self.state == "sql":
            pass
        elif self.state == "fin":
            pass

    def draw(self):
        self.screen.fill(self.BG)
        self.blocnote.draw()
        if self.state == "bureau":
            self.bureau.draw()
            # Temporaire : texte de test
            texte = self.font.render("KING OF THE HACK — bureau", True, self.GREEN)
            self.screen.blit(texte, (20, 20))
        elif self.state == "labyrinthe":
            texte = self.font.render("LABYRINTHE", True, self.GREEN)
            self.screen.blit(texte, (20, 20))
        elif self.state == "phishing":
            texte = self.font.render("PHISHING", True, self.GREEN)
            self.screen.blit(texte, (20, 20))
        elif self.state == "cesar":
            texte = self.font.render("CESAR", True, self.GREEN)
            self.screen.blit(texte, (20, 20))
        elif self.state == "sql":
            texte = self.font.render("SQL", True, self.GREEN)
            self.screen.blit(texte, (20, 20))
        elif self.state == "fin":
            texte = self.font.render("FIN — le virus a disparu", True, self.GREEN)
            self.screen.blit(texte, (20, 20))

