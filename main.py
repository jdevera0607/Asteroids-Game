import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2)
    clock = pygame.time.Clock()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000  # Delta time in seconds.
        player1.update(dt)
        player1.draw(screen)
        clock.tick(60)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
