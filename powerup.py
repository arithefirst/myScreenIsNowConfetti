import random
import pygame


class PowerUp:
    def __init__(self, size, player):
        self.image = pygame.image.load("./images/healthsprite.png").convert_alpha()
        self.player = player
        self.toBeKilled = False

        # Generate random position within screen bounds
        self.x = random.randint(0, size[0] - self.image.get_width())
        self.y = random.randint(0, size[1] - self.image.get_height())

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision(self):
        return self.rect.colliderect(self.player.rect)

    def update(self):
        if self.check_collision():
            if self.player.health < 3:
                self.player.health += 1
                self.toBeKilled = True
