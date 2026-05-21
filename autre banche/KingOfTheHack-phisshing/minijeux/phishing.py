import pygame as p

LIGNE_H  = 64
MARGE    = 10
HEADER_H = 70

# test github
class phishing:

    def __init__(self, screen, font, colors, mails, game):

        self.screen = screen
        self.font   = font
        self.GREEN  = colors["GREEN"]
        self.BG     = colors["BG"]
        self.game   = game

        # Initailisation de la position actuelle à la liste des mails
        self.mails = mails
        self.position_actuelle = mails

        # Des mesures
        w, h = screen.get_width(), screen.get_height()
        panel_w = w - 400

        # Trace des panneaux
        self.rect_panel = p.Rect(0, 0, panel_w, h)
        self.rect_panel2 = p.Rect(0, 50, panel_w, h)
        self.rect_titre = p.Rect(MARGE, MARGE, panel_w - 2*MARGE, 30)
        self.rect_liste = p.Rect(MARGE, HEADER_H, panel_w - 2*MARGE, h - HEADER_H - MARGE)

        # Scroll pour la liste des mails. Comme ça on peut faire défiler s'il y en a trop
        self.scroll_offset = 0
        
        self.mail_ouvert = None



    # Franchement, je sais pas pourquoi il est là encore
    def update(self, dt):
        pass
    
    
    
    # On récupère les items à afficher (les mails)
    def items(self):
        return list(self.position_actuelle.keys())




    def _rect_items(self, index):
        y = self.rect_liste.y + index * LIGNE_H - self.scroll_offset
        return p.Rect(self.rect_liste.x, y, self.rect_liste.width, LIGNE_H - 3)



    def _cliquer(self, nom): # Logique, on ouvre le mail cliqué. Regarde Items et Init
        self.mail_ouvert = self.position_actuelle[nom]



    def handle_event(self, event, game=None):

        if event.type == p.MOUSEBUTTONDOWN and event.button == 1: # Clic gauche

            if self.mail_ouvert is not None:

                if self.rect_retour.collidepoint(event.pos):
                    self.mail_ouvert = None
                return

            for i, nom in enumerate(self.items()): # On regarde tous les items (mails) affichés

                rect = self._rect_items(i) # On calcule le rectangle de chaque mail affiché

                if rect.collidepoint(event.pos) and self.rect_liste.collidepoint(event.pos): # Si on clique sur un mail (et pas en dehors de la liste)
                    self._cliquer(nom)
                    return

        if event.type == p.MOUSEWHEEL: # Scroll de la souris
            if self.rect_panel.collidepoint(p.mouse.get_pos()): 
                self.scroll_offset = max(0, self.scroll_offset - event.y * 20)

    def draw(self):

        p.draw.rect(self.screen, (15, 15, 15), self.rect_panel)
        p.draw.rect(self.screen, self.GREEN, self.rect_panel, 1)

        p.draw.rect(self.screen, self.GREEN, self.rect_panel2, 1)

        self.screen.blit(
            self.font.render("[ PHISHING ]", True, self.GREEN),
            (self.rect_titre.x, self.rect_titre.y)
        )

        if self.mail_ouvert is not None:

            mail = self.mail_ouvert # C'est le mail ouvert, on affiche son contenu

            y = self.rect_panel.y + 80

            # Mise en page / Mise à jour simple du mail, on affiche l'expéditeur, l'objet, puis le corps du mail
            self.screen.blit(
                self.font.render(mail["expediteur"], True, self.GREEN),
                (self.rect_panel.x + 10, y)
            ) 

            self.screen.blit(
                self.font.render(mail["objet"], True, self.GREEN),
                (self.rect_panel.x + 10, y + 30)
            )

            y2 = y + 80

            for line in mail["corps"]:
                self.screen.blit(
                    self.font.render(line, True, self.GREEN),
                    (self.rect_panel.x + 10, y2)
                )
                y2 += 20

            self.rect_retour = p.Rect(
                self.rect_panel.x + 10,
                self.rect_panel.bottom - 50,
                120,
                35
            )

            p.draw.rect(self.screen, (30, 60, 30), self.rect_retour)
            p.draw.rect(self.screen, self.GREEN, self.rect_retour, 1)

            # Super pratique le btn retour. Regarde self.rect_retour et la logique dans handle_event
            self.screen.blit(
                self.font.render("RETURN", True, self.GREEN),
                (self.rect_retour.x + 10, self.rect_retour.y + 8)
            )

            return


        items = self.items()
        souris = p.mouse.get_pos()

        total_h = len(items) * LIGNE_H
        max_scroll = max(0, total_h - self.rect_liste.height)

        # On s'assure que le scroll ne dépasse pas les limites
        self.scroll_offset = max(0, min(self.scroll_offset, max_scroll))

        self.screen.set_clip(self.rect_liste)

        # Liste des mails 
        for i, nom in enumerate(items):

            rect = self._rect_items(i)

            if rect.bottom < self.rect_liste.top or rect.top > self.rect_liste.bottom:
                continue

            if rect.collidepoint(souris):
                p.draw.rect(self.screen, (30, 60, 30), rect)

            mail = self.position_actuelle[nom]

            texte = mail["expediteur"] + " | " + mail["objet"]

            self.screen.blit(
                self.font.render(texte, True, self.GREEN),
                (rect.x + 4, rect.y + 10)
            )

        self.screen.set_clip(None)


        if total_h > self.rect_liste.height:

            ratio = self.rect_liste.height / total_h
            barre_h = max(20, int(self.rect_liste.height * ratio))

            scroll_ratio = self.scroll_offset / max(1, max_scroll)
            barre_y = self.rect_liste.y + int(scroll_ratio * (self.rect_liste.height - barre_h))

            p.draw.rect(
                self.screen,
                self.GREEN,
                p.Rect(self.rect_liste.right - 6, barre_y, 4, barre_h)
            )