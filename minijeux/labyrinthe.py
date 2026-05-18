import pygame as p
from collections import deque


class Noeud:
    """Un dossier ou un fichier dans l'arbre."""
    def __init__(self, nom, est_dossier=True):
        self.nom        = nom
        self.est_dossier = est_dossier
        self.enfants    = []         
        self.parent     = None

    def ajouter_enfant(self, noeud):
        noeud.parent = self
        self.enfants.append(noeud)
        return noeud

    # changement : pour la recherche (parcours en largeur)
    def bfs_recherche(self, nom_cible):
        """Retourne tous les nœuds dont le nom contient nom_cible (insensible à la casse)."""
        resultats = []
        file      = deque([self])
        cible     = nom_cible.lower()
        while file:
            noeud = file.popleft()
            if cible in noeud.nom.lower():
                resultats.append(noeud)
            for enfant in noeud.enfants:
                file.append(enfant)
        return resultats

    def chemin(self):
        """Retourne la liste des ancêtres du plus haut au nœud courant."""
        noeuds = []
        courant = self
        while courant:
            noeuds.append(courant)
            courant = courant.parent
        noeuds.reverse()
        return noeuds



#  Arbre de démo (système de fichiers fictif)


def construire_arbre():
    racine = Noeud("Ordinateur")

    systeme = racine.ajouter_enfant(Noeud("Système"))
    systeme.ajouter_enfant(Noeud("kernel.exe",   est_dossier=False))
    systeme.ajouter_enfant(Noeud("drivers.sys",  est_dossier=False))

    docs = racine.ajouter_enfant(Noeud("Documents"))
    projet = docs.ajouter_enfant(Noeud("Projet_Hack"))
    projet.ajouter_enfant(Noeud("notes.txt",     est_dossier=False))
    projet.ajouter_enfant(Noeud("payload.py",    est_dossier=False))
    secret = projet.ajouter_enfant(Noeud("Secret"))
    secret.ajouter_enfant(Noeud("mot_de_passe.txt", est_dossier=False))
    secret.ajouter_enfant(Noeud("cle_rsa.key",   est_dossier=False))
    docs.ajouter_enfant(Noeud("rapport.pdf",     est_dossier=False))

    reseau = racine.ajouter_enfant(Noeud("Réseau"))
    reseau.ajouter_enfant(Noeud("config.cfg",    est_dossier=False))
    logs = reseau.ajouter_enfant(Noeud("Logs"))
    logs.ajouter_enfant(Noeud("access.log",      est_dossier=False))
    logs.ajouter_enfant(Noeud("error.log",       est_dossier=False))

    return racine





LIGNE_H     = 64   # hauteur d'une ligne d'item
MARGE       = 10
HEADER_H    = 90   # hauteur réservée au fil d'Ariane + barre de recherche


class Explorateur:
    def __init__(self, screen, font, colors):
        self.screen = screen
        self.font   = font
        self.GREEN  = colors["GREEN"]
        self.BG     = colors["BG"]

        self.racine         = construire_arbre()
        self.dossier_actuel = self.racine

        # Barre de recherche
        self.recherche_texte  = ""
        self.recherche_active = False      # True quand le champ est sélectionné
        self.resultats_bfs    = []         # liste de Noeud trouvés
        self.mode_recherche   = False      # affiche les résultats BFS

        # Scroll
        self.scroll_offset = 0

        # Rectangles fixes
        w, h = screen.get_width(), screen.get_height()
        panel_w = w - 400          # laisse la place au blocnote
        self.rect_panel   = p.Rect(0, 0, panel_w, h)
        self.rect_titre   = p.Rect(MARGE, MARGE, panel_w - 2*MARGE, 30)
        self.rect_ariane  = p.Rect(MARGE, 48,    panel_w - 2*MARGE, 24)
        self.rect_search  = p.Rect(MARGE, 64,    panel_w - 2*MARGE, 24)
        self.rect_liste   = p.Rect(MARGE, HEADER_H, panel_w - 2*MARGE, h - HEADER_H - MARGE)

    # helpers 

    def _items_affiches(self):
        """Retourne la liste de Noeud à afficher selon le mode."""
        if self.mode_recherche:
            return self.resultats_bfs
        return self.dossier_actuel.enfants

    def _rect_item(self, index):
        """Rect d'un item dans la liste (avec scroll)."""
        y = self.rect_liste.y + index * LIGNE_H - self.scroll_offset
        return p.Rect(self.rect_liste.x, y, self.rect_liste.width, LIGNE_H - 3)

    def _icone(self, noeud):
        return "[D] " if noeud.est_dossier else "[F] "

    # logique 

    def _ouvrir(self, noeud):
        if noeud.est_dossier:
            self.dossier_actuel = noeud
            self.scroll_offset  = 0
            self.mode_recherche = False
            self.recherche_texte = ""
            self.resultats_bfs   = []

    def _naviguer_vers(self, noeud_ariane):
        """Clic sur le fil d'Ariane : remonte à ce dossier."""
        self.dossier_actuel  = noeud_ariane
        self.scroll_offset   = 0
        self.mode_recherche  = False
        self.recherche_texte = ""
        self.resultats_bfs   = []

    def _lancer_recherche(self):
        if self.recherche_texte.strip():
            self.resultats_bfs  = self.racine.bfs_recherche(self.recherche_texte)
            self.mode_recherche = True
            self.scroll_offset  = 0
        else:
            self.mode_recherche = False

    # interface pygame 

    def handle_event(self, event, game=None):
        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            # Clic barre de recherche
            if self.rect_search.collidepoint(event.pos):
                self.recherche_active = True
                return

            self.recherche_active = False

            # Clic fil d'Ariane
            chemin = self.dossier_actuel.chemin()
            x_ariane = self.rect_ariane.x
            for noeud in chemin:
                label  = noeud.nom + " / "
                largeur = self.font.size(label)[0]
                rect_seg = p.Rect(x_ariane, self.rect_ariane.y, largeur, self.rect_ariane.height)
                if rect_seg.collidepoint(event.pos):
                    self._naviguer_vers(noeud)
                    return
                x_ariane += largeur

            # Clic sur un item de la liste
            items = self._items_affiches()
            for i, noeud in enumerate(items):
                rect = self._rect_item(i)
                if rect.collidepoint(event.pos) and self.rect_liste.collidepoint(event.pos):
                    if self.mode_recherche and noeud.est_dossier:
                        self._naviguer_vers(noeud)
                    elif self.mode_recherche:
                        pass  # fichier en mode recherche : on pourrait l'ouvrir
                    else:
                        self._ouvrir(noeud)
                    return

        # Scroll molette
        if event.type == p.MOUSEWHEEL:
            if self.rect_panel.collidepoint(p.mouse.get_pos()):
                self.scroll_offset = max(0, self.scroll_offset - event.y * LIGNE_H)

        # Saisie barre de recherche
        if event.type == p.KEYDOWN and self.recherche_active:
            if event.key == p.K_BACKSPACE:
                self.recherche_texte = self.recherche_texte[:-1]
                if not self.recherche_texte:
                    self.mode_recherche = False
            elif event.key == p.K_RETURN:
                self._lancer_recherche()
            elif event.key == p.K_ESCAPE:
                self.recherche_texte = ""
                self.mode_recherche  = False
                self.recherche_active = False
            else:
                self.recherche_texte += event.unicode
            return  # on consomme l'événement clavier

    def update(self):
        pass # pas d'animation, tout est dans le draw

    def draw(self):
        # Fond du panel
        p.draw.rect(self.screen, (15, 15, 15), self.rect_panel)
        p.draw.rect(self.screen, self.GREEN,   self.rect_panel, 1)

        # Titre
        titre = "[ EXPLORATEUR DE FICHIERS ]"
        if self.mode_recherche:
            titre += f"  —  Résultats BFS : {len(self.resultats_bfs)}"
        self.screen.blit(self.font.render(titre, True, self.GREEN), (self.rect_titre.x, self.rect_titre.y))

        #  Fil d'Ariane 
        p.draw.line(self.screen, self.GREEN,
                    (self.rect_ariane.x, self.rect_ariane.bottom),
                    (self.rect_ariane.right, self.rect_ariane.bottom), 1)

        chemin   = self.dossier_actuel.chemin()
        x_ariane = self.rect_ariane.x
        souris   = p.mouse.get_pos()
        for noeud in chemin:
            label   = noeud.nom + " / "
            largeur = self.font.size(label)[0]
            rect_seg = p.Rect(x_ariane, self.rect_ariane.y, largeur, self.rect_ariane.height)
            couleur = (255, 255, 0) if rect_seg.collidepoint(souris) else self.GREEN
            self.screen.blit(self.font.render(label, True, couleur), (x_ariane, self.rect_ariane.y))
            x_ariane += largeur

        #  Barre de recherche 
        couleur_search = (255, 255, 0) if self.recherche_active else self.GREEN
        p.draw.rect(self.screen, (25, 25, 25), self.rect_search)
        p.draw.rect(self.screen, couleur_search, self.rect_search, 1)
        contenu = "> " + self.recherche_texte + ("_" if self.recherche_active else "")
        if not self.recherche_texte and not self.recherche_active:
            contenu = "  Rechercher... (cliquer ici, puis Entrée)"
        self.screen.blit(self.font.render(contenu, True, couleur_search), (self.rect_search.x + 4, self.rect_search.y + 3))

        #  Liste des items 
        items   = self._items_affiches()
        max_scroll = max(0, len(items) * LIGNE_H - self.rect_liste.height)
        self.scroll_offset = min(self.scroll_offset, max_scroll)

        # Clip pour ne pas déborder hors du panel
        self.screen.set_clip(self.rect_liste)
        for i, noeud in enumerate(items):
            rect = self._rect_item(i)
            if rect.bottom < self.rect_liste.y or rect.top > self.rect_liste.bottom:
                continue   # hors de la zone visible

            # Survol
            if rect.collidepoint(souris) and self.rect_liste.collidepoint(souris):
                p.draw.rect(self.screen, (30, 60, 30), rect)

            icone = self._icone(noeud)
            label = icone + noeud.nom

            # En mode recherche : affiche le chemin complet sous le nom
            if self.mode_recherche:
                chemin_str = " > ".join(n.nom for n in noeud.chemin())
                couleur_chemin = (100, 180, 100)
                self.screen.blit(
                    self.font.render(chemin_str, True, couleur_chemin),
                    (rect.x + 4, rect.y + 28)
                )

            self.screen.blit(self.font.render(label, True, self.GREEN), (rect.x + 4, rect.y + 2))

        self.screen.set_clip(None)

        # Barre de défilement indicative
        if len(items) * LIGNE_H > self.rect_liste.height:
            ratio      = self.rect_liste.height / (len(items) * LIGNE_H)
            barre_h    = max(20, int(self.rect_liste.height * ratio))
            barre_y    = self.rect_liste.y + int(self.scroll_offset / max_scroll * (self.rect_liste.height - barre_h))
            barre_rect = p.Rect(self.rect_liste.right - 6, barre_y, 4, barre_h)
            p.draw.rect(self.screen, self.GREEN, barre_rect)
