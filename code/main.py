import pygame
import sys 
from player import Player
from crt import CRT
from laser import Laser
from alien import Alien
from obstacle import Obstacle



class Game:
    def __init__(self):

        # Set up the player 
        player_sprite = Player((screen_width/2, screen_height),screen_width,6)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Laser setup 

        # 

    def run(self):
        self.player.draw(screen)
        self.player.update()
        self.player.sprite.laser.draw(screen)


if __name__ == '__main__':
    pygame.init()
    screen_width: int = 600
    screen_height: int = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    crt = CRT(screen, screen_width, screen_height)
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.run()
        #crt.draw()
        clock.tick(60)

        pygame.display.flip()
