"""
    Fichier contenant la classe UIManager.
    Cette classe gère l'interface utilisateur du jeu.
"""

import pygame

from input import InputBox


class UIManager:
    def __init__(self, screen, db_manager, game):
        """
            Constructeur de l'interface Utilisateur (UI User Interface).
            Initialise les variables et les ressources nécessaires.
        """
        self.game = game
        self.screen = screen
        self.db_manager = db_manager
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def main_menu(self):
        """
            Méthode pour afficher le menu principal.
            Affiche les boutons de connexion et d'inscription.
        """
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            login_button = pygame.Rect(100, 100, 200, 50)
            register_button = pygame.Rect(100, 200, 200, 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if login_button.collidepoint(event.pos):
                        self.login_screen()
                    elif register_button.collidepoint(event.pos):
                        self.registration_screen()

            pygame.draw.rect(self.screen, (117, 113, 94), login_button)
            pygame.draw.rect(self.screen, (117, 113, 94), register_button)

            login_text = self.font.render("Connexion", True, (255, 255, 255))
            register_text = self.font.render("Inscription", True, (255, 255, 255))

            self.screen.blit(login_text, (login_button.x + 50, login_button.y + 10))
            self.screen.blit(register_text, (register_button.x + 40, register_button.y + 10))

            pygame.display.flip()
            self.clock.tick(30)

    def login_screen(self):
        """
            Méthode pour afficher l'écran de connexion.
        """

        
        username_label = self.font.render('Pseudo:', True, pygame.Color('white'))
        username_box = InputBox(100, 150, 200, 50)

        password_label = self.font.render('Mot de passe:', True, pygame.Color('white'))
        password_box = InputBox(100, 250, 200, 50)

        button_rect = pygame.Rect(100, 350, 200, 50)
        button_text = self.font.render('Connexion', True, pygame.Color('white'))
        running = True

        while running:
            self.screen.fill((0, 0, 0))  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if button_rect.collidepoint(event.pos):
                        
                        if self.handle_login(username_box.text, password_box.text):
                            print("Utilisateur connecté")
                            self.game.start_game() 
                            running = False

                username_box.handle_event(event)
                password_box.handle_event(event)

            
            self.screen.blit(username_label, (100, username_box.rect.top - 30))
            self.screen.blit(password_label, (100, password_box.rect.top - 30))

            
            username_box.draw(self.screen)
            password_box.draw(self.screen)

            
            pygame.draw.rect(self.screen, pygame.Color('dodgerblue'), button_rect)
            self.screen.blit(button_text, (button_rect.x + 50, button_rect.y + 10))

            pygame.display.flip()

    def registration_screen(self):
        """
            Méthode pour afficher l'écran d'inscription.
        """

        username_label = self.font.render('Pseudo:', True, pygame.Color('white'))
        username_box = InputBox(100, 50, 200, 50)

        name_label = self.font.render('Nom:', True, pygame.Color('white'))
        name_box = InputBox(100, 150, 200, 50)

        surname_label = self.font.render('Prenom:', True, pygame.Color('white'))
        surname_box = InputBox(100, 250, 200, 50)

        password_label = self.font.render('Mot de passe:', True, pygame.Color('white'))
        password_box = InputBox(100, 350, 200, 50)

        button_rect = pygame.Rect(100, 450, 200, 50)  
        button_text = self.font.render('Inscription', True, pygame.Color('white'))
        running = True

        while running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        self.handle_registration(username_box.text, name_box.text, surname_box.text, password_box.text)
                        running = False

                username_box.handle_event(event)
                name_box.handle_event(event)
                surname_box.handle_event(event)
                password_box.handle_event(event)

            
            self.screen.blit(username_label, (100, username_box.rect.top - 30))
            self.screen.blit(name_label, (100, name_box.rect.top - 30))
            self.screen.blit(surname_label, (100, surname_box.rect.top - 30))
            self.screen.blit(password_label, (100, password_box.rect.top - 30))

            
            username_box.draw(self.screen)
            name_box.draw(self.screen)
            surname_box.draw(self.screen)
            password_box.draw(self.screen)

            
            pygame.draw.rect(self.screen, pygame.Color('dodgerblue'), button_rect)
            self.screen.blit(button_text, (button_rect.x + 50, button_rect.y + 10))

            pygame.display.flip()

    def handle_login(self, username, password):
        """
            Méthode pour gérer la connexion.
        """
        user = self.db_manager.check_user(username, password)
        if user:
            print("Connected")
            self.game.current_user_id = user[0]
            return 1
        else :
            print("Invalid username or password")
            return 0


    def handle_registration(self, pseudo, nom, prenom, password):
        """
            Méthode pour gérer l'inscription.
        """
        if self.db_manager.create_user(nom, prenom, pseudo, password):
            self.login_screen()
        else:
            print("Registration failed. Please try again.")