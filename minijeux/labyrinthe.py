import pygame as p


class Labyrinthe():
    def __init__(self, screen, font, colors):
        self.screen = screen
        self.font = font
        self.BG = colors["BG"]
        self.GREEN = colors["GREEN"]
        self.dossier = {"user" : 
            {
            "dossier1": [{"sousDossier1": ["fichier1.txt", "fichier2.txt"]},
                         {"sousDossier2": ["fichier3.txt", "fichier4.txt"]}
                        ],
            "dossier2": [{}],
            "dossier3": [{"sousDossier3": ["fichier5.txt", "fichier6.txt"]}],
            "dossier4": [{"sousDossier4": ["fichier7.txt", "fichier8.txt"]}],
            "dossier5": [{"sousDossier5": ["fichier9.txt", "fichier10.txt"]}]
            }
        }

    def handleEvent(self, event, game):
        
        # Explication : self.dossier = self.dosser["user"] => open dict
        # self.dossier = self.dossier["user"]["dossier1"] => open dict soit sousDossier1
        # etc 

        if self.dossier == self.dossier["user"]:
            pass
        
        if self.dossier == self.dossier["user"]["dossier1"]:
            pass
            if self.dossier == self.dossier["user"]["dossier1"]["sousDossier1"]:
                pass
            elif self.dossier == self.dossier["user"]["dossier1"]["sousDossier2"]:
                pass

        if self.dossier == self.dossier["user"]["dossier2"]:
            pass
            if self.dossier == self.dossier["user"]["dossier2"]["sousDossier2"]:
                pass

        if self.dossier == self.dossier["user"]["dossier3"]:
            pass
            if self.dossier == self.dossier["user"]["dossier3"]["sousDossier3"]:
                pass

        if self.dossier == self.dossier["user"]["dossier4"]:
            pass
            if self.dossier == self.dossier["user"]["dossier4"]["sousDossier4"]:
                pass

        if self.dossier == self.dossier["user"]["dossier5"]:
            pass
            if self.dossier == self.dossier["user"]["dossier5"]["sousDossier5"]:
                pass

    def update(self):
        pass
        

    def draw(self):
        pass