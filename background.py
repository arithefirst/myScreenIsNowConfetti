import pygame


class BackgroundImages:
    def __init__(self, screen):
        self.screen = screen
        self.backgrounds = {
            0: "blue_1.png",
            1: "blue_2.png",
            2: "orange_1.png",
            3: "orange_2.png",
            4: "orange_3.png",
            5: "blue_3.png",
            "ENDLESS": "blue_4.png",
        }

    def draw(self, stage):
        bgImage = pygame.image.load(
            f"./images/backgrounds/{self.backgrounds.get(stage)}"
        )
        bgRect = bgImage.get_rect(topleft=(0, 0))
        self.screen.blit(bgImage, bgRect)
