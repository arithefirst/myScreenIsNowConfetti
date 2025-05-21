import pygame
import sys
from playermove import PlayerMovement

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movement Demo")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create player (blue circle)
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('./images/player.png').convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
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
bgImage = pygame.image.load('./images/bg_texture.png')
bgRect = bgImage.get_rect(topleft=(0,0))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Pass events to the movement handler
        movement.handle_event(event)
    
    # Update player position
    movement.update()
    
    # Keep player within screen bounds
    player.x = max(player.rect.width//2, min(WIDTH - player.rect.width//2, player.x))
    player.y = max(player.rect.height//2, min(HEIGHT - player.rect.height//2, player.y))
    
    # Draw and update
    screen.blit(bgImage, bgRect)
    player.draw(screen)    
    pygame.display.flip()

    
    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
