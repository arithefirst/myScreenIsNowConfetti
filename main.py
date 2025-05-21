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
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x, self.y), self.radius)

# Create player instance
player = Player(WIDTH // 2, HEIGHT // 2, 10)

# Initialize player movement
movement = PlayerMovement(player)

# Game clock
clock = pygame.time.Clock()

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
    player.x = max(player.radius, min(WIDTH - player.radius, player.x))
    player.y = max(player.radius, min(HEIGHT - player.radius, player.y))
    
    # Draw and update
    screen.fill(WHITE)
    player.draw(screen)    
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
