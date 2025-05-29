import pygame
import sys
from playermove import PlayerMovement
from super_evil_bad_guy import BillieEilishBadGuy

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MY SCREEN IS NOW CONFETTI!!!!")


def font(size=72):
    return pygame.font.Font("Comic Sans MS.ttf", size)


isLose = False
score = 0

# Array for multiple enemy spawns
enemies = []
defEnemySpawnInterval = 60
enemySpawnInterval = defEnemySpawnInterval
enemySpawnRampUp = 10
tilNext = enemySpawnInterval
tilNextRamp = 60 * 10
stage = 0


# Create player
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("./images/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.health = 60

    def draw(self, surface):
        self.rect.center = (self.x, self.y)
        surface.blit(self.image, self.rect)


# Create player instance
player = Player(WIDTH // 2, HEIGHT // 2)

# Initialize player movement
movement = PlayerMovement(player)

# Game clock
clock = pygame.time.Clock()

# Set the background image
bgImage = pygame.image.load("./images/bg_texture.png")
bgRect = bgImage.get_rect(topleft=(0, 0))

# Game loop
running = True
while running:
    if not isLose:
        # Spawn a new enemy every 60 frames
        tilNext -= 1
        tilNextRamp -= 1
        if tilNext == 0:
            enemies.append(BillieEilishBadGuy((WIDTH, HEIGHT), player, 20, 7))
            tilNext = enemySpawnInterval

        if tilNextRamp == 0:
            tilNextRamp = 60 * 10
            if enemySpawnInterval > 0:
                enemySpawnInterval -= enemySpawnRampUp
                stage += 1

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Pass events to the movement handler
            movement.handle_event(event)

        # Update player position
        movement.update()

        # Update all enemies
        for i, v in enumerate(enemies):
            v.update()
            if v.checkCollision():
                enemies.pop(i)
                player.health -= 20
                score -= 30
                if player.health == 0:
                    isLose = True
            if v.determineSelfDestruct():
                enemies.pop(i)
                score += 10

        # Keep player within screen bounds
        player.x = max(
            player.rect.width // 2,
            min(WIDTH - player.rect.width // 2, player.x),
        )
        player.y = max(
            player.rect.height // 2,
            min(HEIGHT - player.rect.height // 2, player.y),
        )

        # Draw and update
        screen.blit(bgImage, bgRect)
        player.draw(screen)

        # Stage
        text = font(32).render(f"Stage {stage}", False, (0, 0, 0))
        textRect = text.get_rect()
        screen.blit(text, textRect)

        # Score
        scoreText = font(24).render(f"Score: {score:04d}", False, (0, 0, 0))
        scoreRect = scoreText.get_rect()
        scoreRect.top = 36
        screen.blit(scoreText, scoreRect)

        # Health
        healthText = font(24).render(
            f"Health: {player.health // 20}/3", False, (0, 0, 0)
        )
        healthRect = scoreText.get_rect()
        healthRect.right = 600
        screen.blit(healthText, healthRect)

        # Draw all enemies
        for i in enemies:
            i.draw(screen)

    else:
        # Handle only the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == 114:
                enemies = []
                player = Player(WIDTH // 2, HEIGHT // 2)
                movement = PlayerMovement(player)
                isLose = False
                enemySpawnInterval = defEnemySpawnInterval
                tilNext = defEnemySpawnInterval
                tilNextRamp = 60 * 10
                stage = 0
                score = 0

        screen.fill((0, 0, 0))
        text = font().render("GAME OVER", False, (255, 0, 0))
        restart = font(32).render('Press "r" to restart', False, (255, 0, 0))
        textRect = text.get_rect()
        restartRect = restart.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        restartRect.center = (WIDTH // 2, HEIGHT // 2 + 60)
        screen.blit(text, textRect)
        screen.blit(restart, restartRect)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
