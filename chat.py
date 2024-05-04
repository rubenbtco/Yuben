"""
    Fichier contenant la classe ChatBox.
    (Récupéré en partie sur internet)
"""

import pygame


class ChatBox:
    def __init__(self, x, y, width, height, font):
        """
            Constructeur de la classe ChatBox.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('grey')  # Couleur de fond de l'encadré de chat
        self.text_color = pygame.Color('white')  # Couleur du texte
        self.font = font
        self.messages = []
        self.active = False
        self.input_text = ''
        self.message_limit = 3

    def clear(self):
        """
            Methode pour effacer les messages du tableau.
        """
        self.messages = []


    def add_message(self, message):
        """
            Methode pour ajouter un message au tableau.
        """
        formatted_message = f"{message[0]} : {message[1]}"
        self.messages.append(formatted_message)
        if len(self.messages) > 3:
            self.messages = self.messages[-3:]

    def draw(self, screen):
        """
            Methode pour dessiner les encadrés de chat.
        """

        # Dessiner le fond de l'encadré de chat
        pygame.draw.rect(screen, self.color, self.rect)
        line_height = 20 # Hauteur d'une ligne de texte
        padding = 5 # Espace entre les bords de l'encadré et le texte
        visible_messages = self.messages[-self.message_limit:]
        messages_height = len(visible_messages) * line_height
        start_y = self.rect.y + padding

        # Afficher les messages
        for i, message in enumerate(reversed(visible_messages)):
            text_surface = self.font.render(message, True, self.text_color)
            screen.blit(text_surface, (self.rect.x + padding, start_y + i * line_height))

        # Position de la zone de saisie sous les messages
        input_y = start_y + messages_height + padding
        if self.active:
            input_rect = pygame.Rect(self.rect.x, input_y, self.rect.width, line_height)
            pygame.draw.rect(screen, pygame.Color('darkgrey'), input_rect)
            text_surface = self.font.render(self.input_text + '|', True, self.text_color)  # Ajouter un curseur
            screen.blit(text_surface, (input_rect.x + padding, input_rect.y + 2))

    def toggle(self):
        """
            Methode pour activer ou désactiver le chat.
        """
        self.active = not self.active
        if not self.active:
            self.input_text = ''

    def update_input(self, event):
        """
            Methode pour mettre à jour le texte de la zone de saisie.
        """
        # Si la touche Entrée est pressée, renvoyer le message pour l'envoi.
        if event.key == pygame.K_RETURN:
            message_to_send = self.input_text.strip()
            self.input_text = ''
            self.toggle()
            return message_to_send

        # Si la touche Échap est pressée, réinitialiser le texte et désactiver le chat sans envoyer de message.
        elif event.key == pygame.K_ESCAPE:
            self.input_text = ''
            self.toggle()
            return None

        # Si la touche Retour arrière est pressée, supprimer le dernier caractère.
        elif event.key == pygame.K_BACKSPACE:
            self.input_text = self.input_text[:-1]

        # Sinon, ajouter le caractère tapé à input_text.
        else:
            if len(self.input_text) < 300:
                self.input_text += event.unicode

        return None