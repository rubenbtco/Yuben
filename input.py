"""
    Fichier pour la classe InputBox.
    (Récupérer en partie sur internet)
"""

import pygame

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        """
            Classe pour créer une zone de saisie.
        """
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('dodgerblue2')
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """
            Methode pour gérer les événements de la zone de saisie.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = pygame.Color('dodgerblue') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)  # This can be used to submit the form.
                    return True  # Indicate that Enter was pressed.
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)
        return False

    def draw(self, screen):
        """
            Methode pour dessiner la zone de saisie.
        """
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
