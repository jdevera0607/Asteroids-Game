from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
          random.uniform(20, 50)
          self.velocity.rotate(random.uniform(20, 50))
          old_radius = self.radius
          new_radius = old_radius / 2
          asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
          asteroid1.velocity = self.velocity.rotate(random.uniform(20, 50)) * 1.2
          asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
          asteroid2.velocity = self.velocity.rotate(-random.uniform(20, 50)) * 1.2
          return [asteroid1, asteroid2] 
        else:
            return []