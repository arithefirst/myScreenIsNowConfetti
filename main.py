import pygame
import sys
from playermove import PlayerMovement
from super_evil_bad_guy import BillieEilishBadGuy
from konami import KonamiCodeListener
from particles import ExplosionSystem
import random
import math
from powerup import PowerUp
from background import BackgroundImages

# Initialize pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("earVisuals/good_old_honest_abe.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

# Load sound effects as Sound objects
sound_hit = pygame.mixer.Sound("earVisuals/hurt.wav")
sound_game_over = pygame.mixer.Sound("earVisuals/wompwompwompwomp.mp3")
sound_powerup = pygame.mixer.Sound("earVisuals/powerUp.wav")
sound_stagechange = pygame.mixer.Sound("earVisuals/stageChange.wav")


sound_hit.set_volume(0.4)
sound_game_over.set_volume(0.2)
sound_powerup.set_volume(0.4)
sound_stagechange.set_volume(0.4)

# Set up the display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MY SCREEN IS NOW CONFETTI!!!!")


def font(size=72):
    return pygame.font.Font("Comic Sans MS.ttf", size)


# Game states
GAME_STATE_START = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2

game_state = GAME_STATE_START
invincible = False
score = 0


enemies = []
powerUps = []
defEnemySpawnInterval = 60
enemySpawnInterval = defEnemySpawnInterval
enemySpawnRampUp = 10
tilNext = enemySpawnInterval
tilNextRamp = 60 * 10
enemySpeed = 7
stage = 0
nextPowerUp = random.randint(240, 300)
slow_motion_active = False
slow_motion_timer = 0
original_enemy_speed = enemySpeed


def activate_slow_motion():
    global slow_motion_active, slow_motion_timer, enemySpeed, original_enemy_speed
    if not slow_motion_active:
        original_enemy_speed = enemySpeed
        enemySpeed = enemySpeed / 2
        slow_motion_active = True
        slow_motion_timer = 4.5 * 60
    else:
        return False


# Create player
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("./images/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.health = 3

    def draw(self, surface):
        self.rect.center = (self.x, self.y)
        surface.blit(self.image, self.rect)


def reset_game():
    global enemies, powerUps, explosion_system, player, movement, enemySpawnInterval
    global tilNext, tilNextRamp, stage, score, invincible, nextPowerUp

    enemies = []
    powerUps = []
    explosion_system = ExplosionSystem()
    player = Player(WIDTH // 2, HEIGHT // 2)
    movement = PlayerMovement(player)
    invincible = False
    enemySpawnInterval = defEnemySpawnInterval
    tilNext = defEnemySpawnInterval
    tilNextRamp = 60 * 10
    stage = 0
    score = 0
    nextPowerUp = random.randint(300, 420)


# Create player instance
player = Player(WIDTH // 2, HEIGHT // 2)
movement = PlayerMovement(player)
clock = pygame.time.Clock()
konamiHandler = KonamiCodeListener()
explosion_system = ExplosionSystem()
bg = BackgroundImages(screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == GAME_STATE_START and event.key == pygame.K_SPACE:
                game_state = GAME_STATE_PLAYING
                reset_game()
            elif game_state == GAME_STATE_GAME_OVER and event.key == pygame.K_r:
                game_state = GAME_STATE_PLAYING
                reset_game()

        # Handle movement events during gameplay
        if game_state == GAME_STATE_PLAYING:
            movement.handle_event(event)
            konamiHandler.addKey(event)
            if konamiHandler.checkCode():
                invincible = True

    if game_state == GAME_STATE_START:
        # Start screen
        screen.fill((50, 50, 100))  # Dark blue background

        # Title
        title = font(48).render("MY SCREEN IS NOW", False, (255, 255, 255))
        confetti = font(64).render("CONFETTI!", False, (255, 255, 0))

        # Subtitle
        subtitle = font(24).render("Survive the chaos!", False, (200, 200, 200))

        # Instructions
        start_text = font(32).render("Press SPACE to start", False, (255, 255, 255))
        controls1 = font(20).render(
            "Use WASD or Arrow Keys to move", False, (150, 150, 150)
        )
        controls2 = font(20).render(
            "Collect health power-ups to survive", False, (150, 150, 150)
        )
        musicCredit = font(16).render(
            "(Background music: Strawberry Cake by nobonoko)", False, (150, 150, 150)
        )

        # Position text
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 90))
        confetti_rect = confetti.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        controls1_rect = controls1.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        controls2_rect = controls2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 125))
        musicCredit_rect = musicCredit.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 175))

        # Draw text
        screen.blit(title, title_rect)
        screen.blit(confetti, confetti_rect)
        screen.blit(subtitle, subtitle_rect)
        screen.blit(start_text, start_rect)
        screen.blit(controls1, controls1_rect)
        screen.blit(controls2, controls2_rect)
        screen.blit(musicCredit, musicCredit_rect)

    elif game_state == GAME_STATE_PLAYING:
        # Spawn a new enemy every 60 frames
        tilNext -= 1
        tilNextRamp -= 1
        if tilNext == 0:
            enemies.append(BillieEilishBadGuy((WIDTH, HEIGHT), player, 20, enemySpeed))
            tilNext = enemySpawnInterval

        if tilNextRamp == 0:
            tilNextRamp = 60 * 10
            if enemySpawnInterval > 0 and not stage == 5 and not stage == "ENDLESS":
                enemySpawnInterval -= enemySpawnRampUp
                sound_stagechange.play()
                stage += 1
                enemySpeed += 0.25
            elif stage == 5:
                sound_stagechange.play()
                stage = "ENDLESS"

        if nextPowerUp == 0:
            powerUps.append(
                PowerUp((WIDTH, HEIGHT), player, explosion_system, activate_slow_motion)
            )
            nextPowerUp = random.randint(300, 420)
        else:
            nextPowerUp -= 1

        if slow_motion_active:
            slow_motion_timer -= 1
            if slow_motion_timer <= 0:
                slow_motion_active = False
                enemySpeed = original_enemy_speed

        # Update player position
        movement.update()

        # Update all enemies
        for i, v in enumerate(enemies):
            v.update()
            if v.checkCollision() and not invincible:
                if len(enemies) > 0:
                    enemies.pop(i)
                sound_hit.play()  # Play sound effect without stopping music
                explosion_system.create_explosion(v.x, v.y, v.color)
                player.health -= 1
                score -= 25
                if score < 0:
                    score = 0
                if player.health == 0:
                    game_state = GAME_STATE_GAME_OVER
                    sound_game_over.play()  # Play game over sound
            if v.determineSelfDestruct():
                if len(enemies) > 0:
                    enemies.pop(i)
                score += 10

        # Update power ups
        for i, v in enumerate(powerUps):
            v.update()
            if v.toBeKilled == True and len(powerUps) > 0:
                sound_powerup.play()  # Play powerup sound effect
                powerUps.pop(i)

        # Update explosion system
        explosion_system.update()

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
        bg.draw(stage)
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

        if invincible:
            time = pygame.time.get_ticks() / 200.0  # Slow down the color change
            red = int(127 * (1 + math.sin(time)))
            green = int(127 * (1 + math.sin(time + 2)))
            blue = int(127 * (1 + math.sin(time + 4)))
            rainbow_color = (red, green, blue)

            # Render invincible text
            invincibleText = font(36).render("INVINCIBLE!", False, rainbow_color)
            invincibleRect = invincibleText.get_rect()
            invincibleRect.center = (
                WIDTH // 2,
                HEIGHT - 50,
            )  # Centered, bottom of screen
            screen.blit(invincibleText, invincibleRect)

        # Health
        if not invincible:
            healthText = font(24).render(f"Health: {player.health}/3", False, (0, 0, 0))
            healthRect = scoreText.get_rect()
            healthRect.right = 600
            screen.blit(healthText, healthRect)

        # Draw all enemies
        for i in enemies:
            i.draw(screen)

        for i in powerUps:
            i.draw(screen)

        # Draw explosion particles
        explosion_system.draw(screen)

    elif game_state == GAME_STATE_GAME_OVER:
        screen.fill((247, 147, 140))
        text = font().render("GAME OVER", False, (0, 0, 0))
        restart = font(32).render('Press "r" to restart', False, (0, 0, 0))
        scoreText = font(32).render(f"Score: {score}", False, (0, 0, 0))
        scoreRect = scoreText.get_rect()
        textRect = text.get_rect()
        restartRect = restart.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        restartRect.center = (WIDTH // 2, HEIGHT // 2 + 60)
        scoreRect.center = (WIDTH // 2, HEIGHT // 2 - 60)
        screen.blit(scoreText, scoreRect)
        screen.blit(text, textRect)
        screen.blit(restart, restartRect)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
