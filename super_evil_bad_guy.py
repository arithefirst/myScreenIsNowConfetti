import random as r
import pygame


def get_starting_pos(width, height):
    sides = ["top", "right", "bottom", "left"]
    side = r.choice(sides)

    x, y = 0, 0

    if side == "top":
        x = r.randint(0, width - 1)
        y = 0
    elif side == "bottom":
        x = r.randint(0, width - 1)
        y = height - 1
    elif side == "right":
        x = width - 1
        y = r.randint(0, height - 1)
    else:  # left
        x = 0
        y = r.randint(0, height - 1)

    return (x, y)


class BillieEilishBadGuy:
    def __init__(self, screenSize, player, radius=20, speed=5):
        self.speed = speed
        self.color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
        self.radius = radius
        self.screenSize = screenSize
        self.player = player
        self.targetPos = pygame.Vector2(
            self.screenSize[0] // 2 + r.randint(-50,50), self.screenSize[1] // 2 + r.randint(-50,50)
        )

        startPos = get_starting_pos(screenSize[0], screenSize[1])

        self.x = startPos[0]
        self.y = startPos[1]

    def checkCollision(self):
        # Calculate distance between enemy center and player center
        enemy_center = pygame.Vector2(self.x, self.y)
        player_center = pygame.Vector2(
            self.player.rect.centerx, self.player.rect.centery
        )
        distance = enemy_center.distance_to(player_center)

        # Collision occurs when distance is less than enemy radius plus half player width/height
        collision_distance = (
            self.radius + min(self.player.rect.width, self.player.rect.height) // 2
        )
        return distance < collision_distance

    def determineSelfDestruct(self):
        if pygame.Vector2(self.x, self.y) == self.targetPos:
            if self.radius == 0:
                return True
            else:
                self.radius -= 1
        return False

    def update(self):
        enemyPos = pygame.Vector2(self.x, self.y)
        delta = enemyPos.move_towards(self.targetPos, self.speed)

        self.x = delta[0]
        self.y = delta[1]

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
