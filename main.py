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

# Create player
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
mischievousMale = BillieEilishBadGuy((600, 400), player)

# Initialize player movement
movement = PlayerMovement(player)

# Bounding box
BOUNDS_HEIGHT, BOUNDS_WIDTH = 125, 150
bounds = pygame.Rect((WIDTH // 2) - BOUNDS_WIDTH//2, (HEIGHT // 2) - BOUNDS_HEIGHT//2, BOUNDS_WIDTH,BOUNDS_HEIGHT)

def draw_bound(surface, border=1, border_color=(255, 255, 255)):
    pygame.draw.rect(surface, border_color, bounds, border)

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
    mischievousMale.update()
    
    # Keep player within bounding box
    player.x = max(player.rect.width//2 + bounds.x, min((bounds.width - player.rect.width//2) + bounds.x, player.x))
    player.y = max(player.rect.height//2 + bounds.y, min((bounds.height - player.rect.height//2) + bounds.y, player.y))
    
    # Draw and update
    screen.blit(bgImage, bgRect)
    draw_bound(screen)
    player.draw(screen)    
    mischievousMale.draw(screen)
    pygame.display.flip()

    
    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
