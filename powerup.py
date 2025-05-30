import random
import pygame


class PowerUp:
    def __init__(self, size, player, explosion_system, set_slow):

        powerUpTypes = ["health", "time", "health"]
        self.type = random.choice(powerUpTypes)

        images = {
            "health": "./images/healthsprite.png",
            "time": "./images/hourglass.png",
        }

        self.image = pygame.image.load(images.get(self.type)).convert_alpha()
        self.player = player
        self.toBeKilled = False
        self.explosion_system = explosion_system
        self.set_slow = set_slow

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
            if self.type == "health" and self.player.health < 3:
                self.player.health += 1
                self.toBeKilled = True
                self.explosion_system.create_explosion(self.x, self.y, (255, 0, 0))
            else:
                if self.set_slow() != False:
                    self.toBeKilled = True
                    self.explosion_system.create_explosion(
                        self.x, self.y, (254, 161, 47)
                    )
