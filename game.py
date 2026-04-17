import pygame as p
import setting  as s
# import ennemies as e
import sys 

# fichier jouant le rôle de cerveau central
# il va : lire, mettre à jour et afficher



nouvellePage = False # mettre l'ouverture d'un fichier s'il est vrai 
class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == p.MOUSEBUTTONDOWN:
            if event.button == 1:  # clic gauche
                if self.rect.collidepoint(event.pos):
                    return nouvellePage == True
        return False
    
class Game():
    def __init__(self):
        p.init()
        self.width = 800
        self.height = 900
        self.screen = p.display.set_mode((self.width,self.height)) 
        self.title = p.display.set_caption("HacKing")
        self.running = True
    
    def run(self):
        while self.running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.running = False
                
            # buttonQuit = p.image.load("Interface et menu/Prinbles_Buttons_Analogue_I (v 1.0.1) (9_5_2023)/Prinbles_Buttons_Analogue_I (v 1.0.1) (9_5_2023)/png/Rect-Dark-Default/Exit.png") # chargement de l'image
            # Button.click(buttonQuit, 100, 100)
            p.display.flip()
