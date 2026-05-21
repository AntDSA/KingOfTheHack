import pygame as p

class Blocnote():
    def __init__(self, screen, font, colors):
        self.screen = screen
        self.font = font
        self.GREEN = colors["GREEN"]
        self.BG = colors["BG"]


        # Position et taille — haut droite
        self.largeur = 350
        self.hauteur = 400
        self.x = screen.get_width() - self.largeur - 20
        self.y = 20
        self.rect = p.Rect(self.x, self.y, self.largeur, self.hauteur)

        # Contenu
        self.mission_texte = "En attente d'instructions..."
        self.timer = 0          # en secondes
        self.timer_actif = False
        self.jauge = 0          # 0 à 100
        self.saisie = ""        # ce que le joueur tape

        #boutons 
        self.btn_home = p.Rect(self.x, self.y + self.hauteur + 10, 80, 30)
        self.btn_retour = p.Rect(self.x + 90, self.y + self.hauteur + 10, 80, 30)
        # Boutons de choix de mission
        self.btn_lab = p.Rect(self.x, self.y + self.hauteur + 50, 160, 30)
        self.btn_phi = p.Rect(self.x + 170, self.y + self.hauteur + 50, 160, 30)
        self.afficher_choix = True  # True quand on est sur le bureau sans mission active
        
    def set_mission(self, texte, timer_secondes=0):
        self.mission_texte = texte
        self.timer = timer_secondes
        self.timer_actif = timer_secondes > 0

    def update(self, dt):
        if self.timer_actif and self.timer > 0:
            self.timer -= dt
            if self.timer <= 0:
                self.timer = 0
                self.timer_actif = False

    def handle_event(self, event):
        if event.type == p.KEYDOWN:
            if event.key == p.K_BACKSPACE:
                self.saisie = self.saisie[:-1]
            elif event.key == p.K_RETURN:
                reponse = self.saisie
                self.saisie = ""
                return reponse
            else:
                self.saisie += event.unicode
        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            if self.btn_home.collidepoint(event.pos):
                return "home"
            if self.btn_retour.collidepoint(event.pos):
                return "retour"
            if self.afficher_choix:
                if self.btn_lab.collidepoint(event.pos):
                    return "mission_labyrinthe"
                if self.btn_phi.collidepoint(event.pos):
                    return "mission_phishing"
        return None

    def draw(self):
        # Fond du bloc-note
        p.draw.rect(self.screen, (20, 20, 20), self.rect)
        p.draw.rect(self.screen, self.GREEN, self.rect, 1)

        # Titre
        titre = self.font.render("[ BLOC-NOTE ]", True, self.GREEN)
        self.screen.blit(titre, (self.x + 10, self.y + 10))

        # Séparateur
        p.draw.line(self.screen, self.GREEN,
                    (self.x, self.y + 40),
                    (self.x + self.largeur, self.y + 40), 1)

        # Mission — découpe le texte si trop long
        mots = self.mission_texte.split(" ")
        lignes = []
        ligne_courante = ""
        for mot in mots:
            if self.font.size(ligne_courante + mot)[0] < self.largeur - 20:
                ligne_courante += mot + " "
            else:
                lignes.append(ligne_courante)
                ligne_courante = mot + " "
        lignes.append(ligne_courante)

        for i, ligne in enumerate(lignes):
            texte = self.font.render(ligne, True, self.GREEN)
            self.screen.blit(texte, (self.x + 10, self.y + 55 + i * 25))

        # Timer
        minutes = int(self.timer) // 60
        secondes = int(self.timer) % 60
        timer_str = f"TEMPS : {minutes:02d}:{secondes:02d}"
        couleur_timer = (255, 50, 50) if self.timer < 30 else self.GREEN
        timer_surf = self.font.render(timer_str, True, couleur_timer)
        self.screen.blit(timer_surf, (self.x + 10, self.y + 220))

        # Jauge
        jauge_label = self.font.render(f"PROGRESSION : {int(self.jauge)}%", True, self.GREEN)
        self.screen.blit(jauge_label, (self.x + 10, self.y + 255))
        p.draw.rect(self.screen, (50, 50, 50),
                    p.Rect(self.x + 10, self.y + 280, self.largeur - 20, 15))
        p.draw.rect(self.screen, self.GREEN,
                    p.Rect(self.x + 10, self.y + 280,
                           int((self.largeur - 20) * self.jauge / 100), 15))

        # Champ de saisie
        p.draw.line(self.screen, self.GREEN,
                    (self.x, self.y + 320),
                    (self.x + self.largeur, self.y + 320), 1)
        saisie_label = self.font.render("REPONSE :", True, self.GREEN)
        self.screen.blit(saisie_label, (self.x + 10, self.y + 330))
        saisie_surf = self.font.render("> " + self.saisie + "_", True, self.GREEN)
        self.screen.blit(saisie_surf, (self.x + 10, self.y + 355))

        # Bouton Home
        p.draw.rect(self.screen, (20, 20, 20), self.btn_home)
        p.draw.rect(self.screen, self.GREEN, self.btn_home, 1)
        home_surf = self.font.render("[Home]", True, self.GREEN)
        self.screen.blit(home_surf, (self.btn_home.x + 5, self.btn_home.y + 5))

        # Bouton Retour
        p.draw.rect(self.screen, (20, 20, 20), self.btn_retour)
        p.draw.rect(self.screen, self.GREEN, self.btn_retour, 1)
        retour_surf = self.font.render("[<--]", True, self.GREEN)
        self.screen.blit(retour_surf, (self.btn_retour.x + 5, self.btn_retour.y + 5))
        
        if self.afficher_choix:
            # Bouton Labyrinthe
            p.draw.rect(self.screen, (20, 20, 20), self.btn_lab)
            p.draw.rect(self.screen, self.GREEN, self.btn_lab, 1)
            self.screen.blit(
                self.font.render("[Labyrinthe]", True, self.GREEN),
                (self.btn_lab.x + 5, self.btn_lab.y + 5)
            )
            # Bouton Phishing
            p.draw.rect(self.screen, (20, 20, 20), self.btn_phi)
            p.draw.rect(self.screen, self.GREEN, self.btn_phi, 1)
            self.screen.blit(
                self.font.render("[Phishing]", True, self.GREEN),
                (self.btn_phi.x + 5, self.btn_phi.y + 5)
            )
    def ajouter_points(self, points):
        self.jauge = min(100, self.jauge + points)
        if self.jauge >= 100:
            return "fin"
        return None