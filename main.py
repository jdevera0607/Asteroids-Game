import pygame
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from constants import *
from shooting import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player1 = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2)

    Shot.containers = (updatable, drawable, shots)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
                    print("Asteroid hit!")
            if player1.collide(asteroid):
                print("Collision detected!")
                pygame.quit()
                return

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Delta time in seconds.
        

if __name__ == "__main__":
    main()
