import pygame as p
from data.filesystems import LABYRINTHE_1, LABYRINTHE_2, LABYRINTHE_3

LIGNE_H  = 64
MARGE    = 10
HEADER_H = 70
# encore test github
class Labyrinthe:
    def __init__(self, screen, font, colors, arbre, game):
        self.screen = screen
        self.font   = font
        self.GREEN  = colors["GREEN"]
        self.BG     = colors["BG"]
        self.game   = game

        self.arbre             = arbre
        self.position_actuelle = arbre
        self.historique        = []   # pile pour revenir en arrière
        self.chemin_noms       = []   # noms pour le fil d'Ariane

        self.scroll_offset = 0
        self.message       = ""      # "PERDU !" ou vide

        w, h = screen.get_width(), screen.get_height()
        panel_w = w - 400
        self.rect_panel = p.Rect(0, 0, panel_w, h)
        self.rect_titre = p.Rect(MARGE, MARGE, panel_w - 2*MARGE, 30)
        self.rect_ariane = p.Rect(MARGE, 40, panel_w - 2*MARGE, 24)
        self.rect_liste  = p.Rect(MARGE, HEADER_H, panel_w - 2*MARGE, h - HEADER_H - MARGE)

    def _items(self):
        return list(self.position_actuelle.keys())

    def _rect_item(self, index):
        y = self.rect_liste.y + index * LIGNE_H - self.scroll_offset
        return p.Rect(self.rect_liste.x, y, self.rect_liste.width, LIGNE_H - 3)

    def _cliquer(self, nom):
        valeur = self.position_actuelle[nom]

        if valeur == "GAGNE":
            self.game.blocnote.ajouter_points(self.game.mission_points)
            self.game.missions_faites.append(self.game.mission_active)
            self.game.blocnote.afficher_choix = True
            self.game.set_state("bureau")

        elif valeur == "PERDU":
            self.message = "Mauvaise réponse ! Retour en arrière..."
            if self.historique:
                self.position_actuelle = self.historique.pop()
                self.chemin_noms = self.chemin_noms[:-1]
            else:
                self.position_actuelle = self.arbre
                self.chemin_noms = []
            self.scroll_offset = 0

        elif isinstance(valeur, dict):
            self.historique.append(self.position_actuelle)
            self.chemin_noms.append(nom)
            self.position_actuelle = valeur
            self.scroll_offset = 0
            self.message = ""

    def handle_event(self, event, game=None):
        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            items = self._items()
            for i, nom in enumerate(items):
                rect = self._rect_item(i)
                if rect.collidepoint(event.pos) and self.rect_liste.collidepoint(event.pos):
                    self._cliquer(nom)
                    return

        if event.type == p.MOUSEWHEEL:
            if self.rect_panel.collidepoint(p.mouse.get_pos()):
                self.scroll_offset = max(0, self.scroll_offset - event.y * LIGNE_H)

    def update(self):
        pass

    def draw(self):
        p.draw.rect(self.screen, (15, 15, 15), self.rect_panel)
        p.draw.rect(self.screen, self.GREEN, self.rect_panel, 1)

        # Titre
        self.screen.blit(
            self.font.render("[ LABYRINTHE DE FICHIERS ]", True, self.GREEN),
            (self.rect_titre.x, self.rect_titre.y)
        )

        # Fil d'Ariane
        ariane = "racine / " + " / ".join(self.chemin_noms)
        self.screen.blit(
            self.font.render(ariane, True, (100, 180, 100)),
            (self.rect_ariane.x, self.rect_ariane.y)
        )
        p.draw.line(self.screen, self.GREEN,
                    (self.rect_ariane.x, self.rect_ariane.bottom),
                    (self.rect_ariane.right, self.rect_ariane.bottom), 1)

        # Message PERDU
        if self.message:
            self.screen.blit(
                self.font.render(self.message, True, (255, 50, 50)),
                (self.rect_liste.x, self.rect_liste.y - 20)
            )

        # Liste des dossiers
        items  = self._items()
        souris = p.mouse.get_pos()

        max_scroll = max(0, len(items) * LIGNE_H - self.rect_liste.height)
        self.scroll_offset = min(self.scroll_offset, max_scroll)

        self.screen.set_clip(self.rect_liste)
        for i, nom in enumerate(items):
            rect = self._rect_item(i)
            if rect.bottom < self.rect_liste.y or rect.top > self.rect_liste.bottom:
                continue

            if rect.collidepoint(souris) and self.rect_liste.collidepoint(souris):
                p.draw.rect(self.screen, (30, 60, 30), rect)

            valeur = self.position_actuelle[nom]
            icone = "[D] " if isinstance(valeur, dict) else "[F] "
            self.screen.blit(
                self.font.render(icone + nom, True, self.GREEN),
                (rect.x + 4, rect.y + 2)
            )
        self.screen.set_clip(None)

        # Barre de scroll
        if len(items) * LIGNE_H > self.rect_liste.height and max_scroll > 0:
            ratio   = self.rect_liste.height / (len(items) * LIGNE_H)
            barre_h = max(20, int(self.rect_liste.height * ratio))
            barre_y = self.rect_liste.y + int(self.scroll_offset / max_scroll * (self.rect_liste.height - barre_h))
            p.draw.rect(self.screen, self.GREEN, p.Rect(self.rect_liste.right - 6, barre_y, 4, barre_h))