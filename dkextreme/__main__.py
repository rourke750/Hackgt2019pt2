from . import entities as ent
import pygame
from . import util
from .entities import Platform, Barrel


def main():
    pygame.init()
    pygame.display.set_caption("minimal program")

    screenX, screenY = util.screenX, util.screenY

    screen = pygame.display.set_mode((screenX, screenY))
    image = pygame.image.load("img/player.png")

    print(image.get_rect().size) 

    x,y = 0,0
    screen.blit(image, (50,50))
    pygame.display.flip()

    running = True
    moveLeft = False
    moveRight = False
    
    all = pg.sprite.RenderUpdates()
    barrels = pg.sprite.Group()
    players = pg.sprite.Group()
    
    
    Platform.containers = all, barrels

    # Build the platforms
    
    
    while running:
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moveLeft = True
                elif event.key == pygame.K_d:
                    moveRight = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    # move left
                    moveLeft = False
                elif event.key == pygame.K_d:
                    # move right
                    moveRight = False
        screen.fill((0,0,0))
        pygame.display.update()

if __name__ == '__main__':
    main()