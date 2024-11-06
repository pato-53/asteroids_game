import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exits the game loop
        screen.fill((0, 0, 0))  # RGB for black

        # Refresh the display
        pygame.display.flip()

if __name__ == "__main__":
    main()