import pygame


class KonamiCodeListener:
    def __init__(self):
        self.keys = []

    def addKey(self, event):
        if event.type == pygame.KEYDOWN:
            if len(self.keys) == 11:
                self.keys.pop(0)
            self.keys.append(event.key)

    def checkCode(self):
        return (
            len(self.keys) == 11
            and self.keys[0] == pygame.K_UP
            and self.keys[1] == pygame.K_UP
            and self.keys[2] == pygame.K_DOWN
            and self.keys[3] == pygame.K_DOWN
            and self.keys[4] == pygame.K_LEFT
            and self.keys[5] == pygame.K_RIGHT
            and self.keys[6] == pygame.K_LEFT
            and self.keys[7] == pygame.K_RIGHT
            and self.keys[8] == pygame.K_b
            and self.keys[9] == pygame.K_a
            and self.keys[10] == pygame.K_RETURN
        )
