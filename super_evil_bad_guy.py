import random as r
import pygame


def get_starting_pos(width, height):
    sides = ["top", "right", "bottom", "left"]
    side = r.choice(sides)

    x = 0
    y = 0

    if side == "top" or side == "bottom":
        x = r.randint(0, width)
    else:
        y = r.randint(0, height)

    return (x, y)


class BillieEilishBadGuy:
    def __init__(self, screenSize, radius=20, speed=5):
        self.speed = speed
        self.color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
        self.radius = radius
        self.screenSize = screenSize

        startPos = get_starting_pos(screenSize[0], screenSize[1])

        self.x = startPos[0]
        self.y = startPos[1]

    def update(self):
        enemyPos = pygame.Vector2(self.x, self.y)
        targetPos = pygame.Vector2(self.screenSize[0] // 2, self.screenSize[1] // 2)
        delta = enemyPos.move_towards(targetPos, self.speed)

        self.x = delta[0]
        self.y = delta[1]
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
