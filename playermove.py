import pygame


class PlayerMovement:
    def __init__(self, player, speed=5):
        self.player = player
        self.speed = speed
        self.movement = {"up": False, "down": False, "left": False, "right": False}

    def handle_event(self, event):
        # Handle key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.movement["up"] = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.movement["down"] = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.movement["left"] = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.movement["right"] = True

        # Handle key release events
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.movement["up"] = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.movement["down"] = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.movement["left"] = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.movement["right"] = False

    def update(self):
        # If shift is being held, cut the speed in half
        keyStates = pygame.key.get_pressed()
        localSpeed = (
            self.speed / 2
            if keyStates[pygame.K_LSHIFT] or keyStates[pygame.K_RSHIFT]
            else self.speed
        )

        # Handle vertical movement
        if self.movement["up"]:
            self.player.y -= localSpeed
        if self.movement["down"]:
            self.player.y += localSpeed

        # Handle horizontal movement
        if self.movement["left"]:
            self.player.x -= localSpeed
        if self.movement["right"]:
            self.player.x += localSpeed
