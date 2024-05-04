"""
    Fichier principal du jeu.
    Il contient la boucle du jeu et les fonctions pour gérer les événements.
"""

import pygame
import pyscroll
import pytmx

from chat import ChatBox
from database import DatabaseManager
from ui import UIManager


class Game:
    def __init__(self):
        """
            Constructeur de la classe Game.
            Initialise les variables et charge les ressources nécessaires.
            Gère la connexion à la base de données.
        """

        pygame.init()
        self.current_user_id = None
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mon Jeu")

        # LOCALHOST
        self.db_manager = DatabaseManager('localhost', 'root', '','nsi_eleve6')

        # Serveur du prof
        #self.db_manager = DatabaseManager('0504-srv-sig', 'nsi_eleve6', 'eleve6', 'nsi_eleve6')

        self.ui_manager = UIManager(self.screen, self.db_manager,self)

        self.font = pygame.font.Font(None, 24)
        self.chat_box = ChatBox(10, 500, 480, 40, self.font)
        self.last_message_update = pygame.time.get_ticks()
    def start(self):
        """
            Methode pour démarrer le menu afin de se connecter ou s'inscrire.
        """
        self.ui_manager.main_menu()

    def start_game(self):
        """
            Methode pour démarrer le jeu et charge la carte.
        """
        self.running = True
        self.load_map("data/maps/map1.tmx")
        self.run()

    def run(self):
        """
            Boucle principale du jeu.
        """
        while self.running:
            self.handle_events()
            if not self.chat_box.active:  # si le chat n'est pas actif, update le jeu
                self.update()
            self.update_chat()
            self.group.update()
            self.group.draw(self.screen)
            self.chat_box.draw(self.screen)  # Assurez-vous que c'est après le dessin du groupe
            pygame.display.flip()

    def update(self):
        """
            Methode pour mettre à jour le jeu.
            Elle pertmet de gérer les déplacements du joueur.
        """
        keys = pygame.key.get_pressed()
        speed = 1
        if not self.chat_box.active:
            if keys[pygame.K_z]:
                self.player.rect.y -= speed
                self.change_direction('up')

            if keys[pygame.K_q]:
                self.player.rect.x -= speed
                self.change_direction('left')

            if keys[pygame.K_s]:
                self.player.rect.y += speed
                self.change_direction('down')

            if keys[pygame.K_d]:
                self.player.rect.x += speed
                self.change_direction('right')

        self.group.center(self.player.rect.center)

    def update_chat(self):
        """
            Methode pour mettre à jour le chat.
            Elle permet de récupérer les messages de la base de données et les afficher.
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_message_update > 1500:  # (1.5 secondes)
            messages = self.db_manager.get_messages()
            self.chat_box.clear()
            for message in messages:
                self.chat_box.add_message(message)
            self.last_message_update = current_time

    def handle_events(self):
        """
            Methode pour gérer les événements.
            Elle permet de gérer les événements de la fenêtre et les touches du clavier.
        """
        # Pour chaque événement dans la liste des événements
        for event in pygame.event.get():

            # Si l'événement est de type QUIT
            if event.type == pygame.QUIT:
                self.running = False

            # Si on appui sur une touche
            elif event.type == pygame.KEYDOWN:
                if self.chat_box.active: # Si le chat est actif, n'utilisez que les touches pour le chat

                    # Fermer le chat avec Échap
                    if event.key == pygame.K_ESCAPE:
                        self.chat_box.toggle()

                    # Envoyer le message avec ENTER
                    elif event.key == pygame.K_RETURN:
                        message = self.chat_box.input_text

                        # On vérifie si le message n'est pas vide et que l'utilisateur est connecté
                        if self.current_user_id is not None and message != '':
                            self.db_manager.send_message(self.current_user_id, message)
                        self.chat_box.input_text = ''
                        self.chat_box.toggle()

                    # Écrire le message
                    else:
                        self.chat_box.update_input(event)


                else:  # Si le chat n'est pas actif, utilisez les touches pour d'autres contrôles
                    # Fermer le jeu avec Échap
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                    # Ouvrir le chat avec T
                    elif event.key == pygame.K_t:
                        # Ouvrir le chat si T est pressé
                        self.chat_box.toggle()

    def load_map(self, filename):
        """
            Methode pour charger la carte et le joueur.
        """

        # Chargement de la map
        tmx_data = pytmx.util_pygame.load_pygame(filename)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.map_layer = map_layer
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

        # Ajout du joueur
        try:
            player_position = tmx_data.get_object_by_name("PlayerStart")
            start_position = (player_position.x, player_position.y)
        except ValueError:
            # Position par défaut
            start_position = (100, 100)

        # Chargement de l'image du personnage
        player_image_path = 'assets/Modern tiles_Free/Characters_free/Adam_idle_16x16.png'
        sprite_sheet = pygame.image.load(player_image_path).convert_alpha()

        self.player_sprites = {
            'down': sprite_sheet.subsurface((48, 0, 16, 32)),
            'left': sprite_sheet.subsurface((32, 0, 16, 32)),
            'right': sprite_sheet.subsurface((0, 0, 16, 32)),
            'up': sprite_sheet.subsurface((16, 0, 16, 32)),
        }
        self.current_direction = 'down'
        self.player = pygame.sprite.Sprite()
        self.player.image = self.player_sprites[self.current_direction]
        self.player.rect = self.player.image.get_rect(center=start_position)
        self.group.add(self.player)

    def change_direction(self, direction):
        """
            Methode pour changer la direction du joueur.
        """
        if direction in self.player_sprites:
            self.current_direction = direction
            self.player.image = self.player_sprites[direction]





