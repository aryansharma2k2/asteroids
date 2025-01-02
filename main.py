from constants import *
import pygame
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        screen.fill(color="black")
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        dt = clock.tick(60)/1000

main()