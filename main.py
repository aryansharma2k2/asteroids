from constants import *
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    while True:
        screen.fill(color="black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()

main()