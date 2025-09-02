from circleshape import CircleShape
from constants import *
from shooting import Shot
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # degrees
        self.time_since_last_shot = 0
       
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.time_since_last_shot > 0:
            self.time_since_last_shot -= dt

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt

        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)  
        if keys[pygame.K_SPACE] and self.time_since_last_shot <= 0:
            shot = self.shoot()
            self.time_since_last_shot = PLAYER_SHOOT_COOLDOWN
            return shot 
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
      
        # print(f"Player position: {self.position}, rotation: {self.rotation}")

        # Update position based on velocity and delta time
        # self.position += self.velocity * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity = forward * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y, self.rotation)
        shot.velocity = self.velocity
        return shot