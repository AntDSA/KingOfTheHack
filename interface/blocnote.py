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

    def set_mission(self, texte, timer_secondes=0):
        self.mission_texte = texte
        self.timer = timer_secondes
        self.timer_actif = timer_secondes > 0

    def ajouter_points(self, points):
        self.jauge = min(100, self.jauge + points)

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
                return reponse  # renvoie la réponse au gestionnaire
            else:
                self.saisie += event.unicode
        return None

    def draw(self):
        # Fond du bloc-note
        p.draw.rect(self.screen, (20, 20, 20), self.rect)
        p.draw.rect(self.screen, self.GREEN, self.rect, 1)

        # Titre
        titre = self.font.render("[ BLOC-NOTE VIRUS ]", True, self.GREEN)
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