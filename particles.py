import pygame
import random
import math


class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        # Random velocity in all directions
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 8)
        self.vel_x = math.cos(angle) * speed
        self.vel_y = math.sin(angle) * speed
        self.size = random.randint(2, 6)
        self.life = random.randint(20, 40)  # frames
        self.max_life = self.life

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_x *= 0.98  # friction
        self.vel_y *= 0.98
        self.life -= 1

    def draw(self, surface):
        if self.life > 0:
            # Fade out over time
            alpha = int(255 * (self.life / self.max_life))
            fade_color = (*self.color[:3], alpha)
            # Create a surface for alpha blending
            temp_surface = pygame.Surface(
                (self.size * 2, self.size * 2), pygame.SRCALPHA
            )
            pygame.draw.circle(
                temp_surface, fade_color, (self.size, self.size), self.size
            )
            surface.blit(temp_surface, (self.x - self.size, self.y - self.size))

    def is_alive(self):
        return self.life > 0


class ExplosionSystem:
    def __init__(self):
        self.particles = []

    def create_explosion(self, x, y, color, particle_count=15):
        for _ in range(particle_count):
            self.particles.append(Particle(x, y, color))

    def update(self):
        # Update all particles and remove dead ones
        self.particles = [p for p in self.particles if p.is_alive()]
        for particle in self.particles:
            particle.update()

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)
